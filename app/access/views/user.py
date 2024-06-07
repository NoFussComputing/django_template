from django.contrib.auth import decorators as auth_decorator
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic

from access.mixin import OrganizationPermission
from access.models import Team, TeamUsers



class Add(OrganizationPermission, generic.CreateView):
    model = TeamUsers
    parent_model = Team
    permission_required = [
        'access.view_team',
        'access.add_teamusers'
    ]
    template_name = 'form.html.j2'
    fields = [
        'user',
        'manager'
    ]


    def form_valid(self, form):
        team = Team.objects.get(pk=self.kwargs['pk'])
        form.instance.team = team

        return super().form_valid(form)


    def get_success_url(self, **kwargs):

        return reverse('Access:_team_view', 
            kwargs={
                'organization_id': self.kwargs['organization_id'],
                'pk': self.kwargs['pk']
            }
        )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['content_title'] = 'Add Team User'

        return context


class Delete(OrganizationPermission, generic.DeleteView):
    model = TeamUsers
    permission_required = [
        'access.delete_teamusers'
    ]
    template_name = 'form.html.j2'


    def get_success_url(self, **kwargs):

        return reverse('Access:_team_view', 
            kwargs={
                'organization_id': self.kwargs['organization_id'],
                'pk': self.kwargs['team_id']
            }
        )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['content_title'] = 'Delete Team User'

        return context
