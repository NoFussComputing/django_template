from django.contrib.auth.models import Permission

from rest_framework import generics, routers, serializers, views
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.response import Response

from access.mixin import OrganizationMixin
from access.models import Organization, Team

from api.serializers.access import OrganizationSerializer, OrganizationListSerializer, TeamSerializer
from api.views.mixin import OrganizationPermissionAPI



class OrganizationList(generics.ListCreateAPIView):

    permission_classes = [
        OrganizationPermissionAPI
    ]

    queryset = Organization.objects.all()
    lookup_field = 'pk'
    serializer_class = OrganizationListSerializer


    def get_view_name(self):
        return "Organizations"



class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [
        OrganizationPermissionAPI
    ]

    queryset = Organization.objects.all()
    lookup_field = 'pk'
    serializer_class = OrganizationSerializer


    def get_view_name(self):
        return "Organization"



class TeamList(generics.ListCreateAPIView):

    permission_classes = [
        OrganizationPermissionAPI
    ]

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


    def get_queryset(self):

        self.queryset = Team.objects.filter(organization=self.kwargs['organization_id'])

        return self.queryset


    def get_view_name(self):
        return "Organization Teams"



class TeamDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [
        OrganizationPermissionAPI
    ]

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    lookup_field = 'group_ptr_id'



class TeamPermissionDetail(routers.APIRootView):

    # temp disabled until permission checker updated
    # permission_classes = [
    #     OrganizationPermissionAPI
    # ]


    def get(self, request, *args, **kwargs):

        return Response(data=Team.objects.get(pk=self.kwargs['group_ptr_id']).permission_list()[0])


    def get_view_name(self):
        return "Team Permissions"


    def delete(self, request, *args, **kwargs):

        vals = self.process_request()

        remove = vals['remove']

        new_permission = Team.objects.get(pk=self.kwargs['group_ptr_id'])


        for remove_permission in remove:
            new_permission.permissions.remove(remove_permission)
            new_permission.save()

        return Response(data=Team.objects.get(pk=self.kwargs['group_ptr_id']).permission_list()[0])


    def patch(self, request, *args, **kwargs):

        vals = self.process_request()

        add = vals['add']

        new_permission = Team.objects.get(pk=self.kwargs['group_ptr_id'])

        for add_permission in add:
            new_permission.permissions.add(add_permission)
            new_permission.save()


        return Response(data=Team.objects.get(pk=self.kwargs['group_ptr_id']).permission_list()[0])


    def post(self, request, *args, **kwargs):

        vals = self.process_request()

        add = vals['add']
        remove = vals['remove']
        exists = vals['exists']

        new_permission = Team.objects.get(pk=self.kwargs['group_ptr_id'])

        for add_permission in add:
            new_permission.permissions.add(add_permission)
            new_permission.save()

        for remove_permission in remove:
            new_permission.permissions.remove(remove_permission)
            new_permission.save()


        return Response(data=Team.objects.get(pk=self.kwargs['group_ptr_id']).permission_list()[0])


    def process_request(self) -> dict({
        "add": list,
        "remove": list,
        "exists": list
    }):

        initial_values = Team.objects.get(pk=self.kwargs['group_ptr_id']).permission_list()

        add = []
        remove = []
        exists = []


        for request_permission in self.request.data:

            fields = request_permission.split('.')

            try:

                permission = Permission.objects.get(codename=str(fields[1]), content_type__app_label=str(fields[0]))

                exists += [ permission.id ]

                if permission and request_permission not in initial_values[0]:
                    add += [ permission.id ]

            except:

                raise serializers.ValidationError(f'Value was invalid: {request_permission}')

        for existing_permission in initial_values[1].all():

            if existing_permission.id not in add and existing_permission.id not in exists:
                remove += [ existing_permission.id ] 

        return {
            "add": add,
            "remove": remove,
            "exists": exists
        }
