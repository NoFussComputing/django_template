from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic

from access.mixin import OrganizationPermission

from itam.models.software import SoftwareCategory


class Index(PermissionRequiredMixin, OrganizationPermission, generic.ListView):

    model = SoftwareCategory

    permission_required = 'itam.view_software'

    template_name = 'settings/software_categories.html.j2'

    context_object_name = "list"

    paginate_by = 10


    def get_queryset(self):

        if self.request.user.is_superuser:

            return self.model.objects.filter().order_by('name')

        else:

            return self.model.objects.filter(organization=self.user_organizations()).order_by('name')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['content_title'] = 'Software Categories'

        return context
