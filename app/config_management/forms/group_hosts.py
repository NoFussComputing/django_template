from django import forms

from itam.models.device import Device

from config_management.models.groups import ConfigGroups, Hosts


class ConfigGroupHostsForm(forms.ModelForm):

    __name__ = 'asdsa'

    class Meta:

        fields = [
            'host'
        ]

        model = Hosts

    prefix = 'config_group_hosts'
