from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.views import generic

from access.mixin import OrganizationPermission

from itam.models.device import DeviceSoftware
from itam.models.software import Software, SoftwareVersion
from itam.forms.software.update import Update as SoftwareUpdate_Form

class IndexView(PermissionRequiredMixin, OrganizationPermission, generic.ListView):
    model = Software
    permission_required = 'itam.view_software'
    template_name = 'itam/software_index.html.j2'
    context_object_name = "softwares"
    paginate_by = 10


    def get_queryset(self):

        if self.request.user.is_superuser:

            return Software.objects.filter().order_by('name')

        else:

            return Software.objects.filter(Q(organization__in=self.user_organizations()) | Q(is_global = True)).order_by('name')




class View(OrganizationPermission, generic.UpdateView):
    model = Software
    permission_required = [
        'itam.view_software'
    ]
    template_name = 'itam/software.html.j2'

    form_class = SoftwareUpdate_Form

    context_object_name = "software"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        software_versions = SoftwareVersion.objects.filter(software=self.kwargs['pk'])

        context['software_versions'] = software_versions

        context['content_title'] = self.object.name

        if self.request.user.is_superuser:
            context['device_software'] = DeviceSoftware.objects.filter(software=self.kwargs['pk']).order_by('device', 'organization')
        elif not self.request.user.is_superuser:
            context['device_software'] = DeviceSoftware.objects.filter(Q(device__in=self.user_organizations(), software=self.kwargs['pk'])).order_by('name', 'organization')

        return context

    def get_success_url(self, **kwargs):

        return f"/itam/software/{self.kwargs['pk']}/"



class Add(PermissionRequiredMixin, OrganizationPermission, generic.CreateView):
    model = Software
    permission_required = [
        'access.add_software',
    ]
    template_name = 'form.html.j2'
    fields = [
        'name',
        'category',
        'organization',
        'is_global'
    ]


    def get_success_url(self, **kwargs):

        return f"/itam/software/"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['content_title'] = 'Add Software'

        return context

class Delete(PermissionRequiredMixin, OrganizationPermission, generic.DeleteView):
    model = Software
    permission_required = [
        'access.delete_software',
    ]
    template_name = 'form.html.j2'

    def get_success_url(self, **kwargs):

        return f"/itam/software/"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['content_title'] = 'Delete ' + self.object.name

        return context