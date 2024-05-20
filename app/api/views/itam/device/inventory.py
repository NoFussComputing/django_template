# from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
import json
import re

from django.http import JsonResponse
from django.utils import timezone

from rest_framework import generics, views
from rest_framework.response import Response

from access.models import Organization

from core.http.common import Http

from itam.models.device import Device, DeviceType, DeviceOperatingSystem, DeviceSoftware
from itam.models.operating_system import OperatingSystem, OperatingSystemVersion
from itam.models.software import Software, SoftwareCategory, SoftwareVersion



class Collect(views.APIView):

    def post(self, request, *args, **kwargs):

        data = json.loads(request.body)

        status = Http.Status.BAD_REQUEST
        
        device = None
        device_operating_system = None
        operating_system = None
        operating_system_version = None

        organization = Organization.objects.get(pk=1)

        try:

            if Device.objects.filter(name=data['details']['name']).exists():

                device = Device.objects.get(name=data['details']['name'])
    
            else: # Create the device

                device = Device.objects.create(
                    name = data['details']['name'],
                    device_type = DeviceType.objects.get(pk=1),
                    serial_number = data['details']['serial_number'],
                    uuid = data['details']['uuid'],
                    organization = organization,
                )

                status = Http.Status.CREATED


            if OperatingSystem.objects.filter( slug=data['os']['name'] ).exists():

                operating_system = OperatingSystem.objects.get( slug=data['os']['name'] )

            else: # Create Operating System

                operating_system = OperatingSystem.objects.create(
                    name = data['os']['name'],
                    organization = device.organization,
                    is_global = True
                )


            if OperatingSystemVersion.objects.filter( name=data['os']['version_major'], operating_system=operating_system ).exists():

                operating_system_version = OperatingSystemVersion.objects.get(
                    organization = device.organization,
                    is_global = True,
                    name = data['os']['version_major'],
                    operating_system = operating_system
                )

            else: # Create Operating System Version

                operating_system_version = OperatingSystemVersion.objects.create(
                    organization = device.organization,
                    is_global = True,
                    name = data['os']['version_major'],
                    operating_system = operating_system,
                )


            if DeviceOperatingSystem.objects.filter( version=data['os']['version'], device=device, operating_system_version=operating_system_version ).exists():

                device_operating_system = DeviceOperatingSystem.objects.get(
                    device=device,
                    version = data['os']['version'],
                    operating_system_version = operating_system_version,
                )

                if not device_operating_system.installdate: # Only update install date if empty

                    device_operating_system.installdate = timezone.now()

                    device_operating_system.save()

            else: # Create Operating System Version

                device_operating_system = DeviceOperatingSystem.objects.create(
                    organization = device.organization,
                    device=device,
                    version = data['os']['version'],
                    operating_system_version = operating_system_version,
                    installdate = timezone.now()
                )


            for inventory in list(data['software']):

                software = None
                software_category = None
                software_version = None

                device_software = None


                if SoftwareCategory.objects.filter( name = inventory['category'] ).exists():

                    software_category = SoftwareCategory.objects.get(
                        name = inventory['category']
                    )

                else: # Create Software Category

                    software_category = SoftwareCategory.objects.create(
                        organization = device.organization,
                        is_global = True,
                        name = inventory['category'],
                    )


                if Software.objects.filter( name = inventory['name'] ).exists():

                    software = Software.objects.get(
                        name = inventory['name']
                    )

                    if not software.category:

                        software.category = software_category
                        software.save()

                else: # Create Software

                    software = Software.objects.create(
                        organization = device.organization,
                        is_global = True,
                        name = inventory['name'],
                        category = software_category,
                    )


                pattern = r"^(\d+:)?(?P<semver>\d+\.\d+(\.\d+)?)"

                semver = re.search(pattern, str(inventory['version']), re.DOTALL)


                if semver:

                    semver = semver['semver']

                else:
                    semver = inventory['version']


                if SoftwareVersion.objects.filter( name = semver, software = software ).exists():

                    software_version = SoftwareVersion.objects.get(
                        name = semver,
                        software = software,
                    )

                else: # Create Software Category

                    software_version = SoftwareVersion.objects.create(
                        organization = device.organization,
                        is_global = True,
                        name = semver,
                        software = software,
                    )


                if DeviceSoftware.objects.filter( software = software, device=device ).exists():

                    device_software = DeviceSoftware.objects.get(
                        device = device,
                        software = software
                    )

                else: # Create Software

                    device_software = DeviceSoftware.objects.create(
                        organization = device.organization,
                        is_global = True,
                        installedversion = software_version,
                        software = software,
                        device = device,
                        action=None
                    )


                if device_software: # Update the Inventoried software

                    clear_installed_software = DeviceSoftware.objects.filter(
                        device = device,
                        software = software
                    )

                    # Clear installed version of all installed software
                    # any found later with no version to be removed
                    clear_installed_software.update(installedversion=None)


                    if not device_software.installed: # Only update install date if blank

                        device_software.installed = timezone.now()

                        device_software.save()

                    device_software.installedversion = software_version

                    device_software.save()


            if device and operating_system and operating_system_version and device_operating_system:

                # Remove software no longer installed
                DeviceSoftware.objects.filter(
                    device = device,
                    software = software,
                ).delete()

                device.inventorydate = timezone.now()

                device.save()

                status = Http.Status.OK


        except Exception as e:

            print(f'An error occured{e}')

            status = Http.Status.SERVER_ERROR


        return Response(data='OK',status=status)



    def get_view_name(self):
        return "Inventory"