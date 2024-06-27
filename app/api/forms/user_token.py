import datetime
from django import forms

from api.models.tokens import AuthToken

from app import settings



class AuthTokenForm(forms.ModelForm):

    prefix = 'user_token'

    class Meta:

        fields = [
            'note',
            'expires',
        ]

        model = AuthToken


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['expires'].widget = forms.widgets.DateTimeInput(attrs={'type': 'datetime-local', 'format': "%Y-%m-%dT%H:%M"})
        self.fields['expires'].input_formats = settings.DATETIME_FORMAT
        self.fields['expires'].format="%Y-%m-%dT%H:%M"
        self.fields['expires'].initial= datetime.datetime.now() + datetime.timedelta(days=90)


        self.fields['generated_token'] = forms.CharField(
            label="Generated Token",
            initial=self.instance.generate(),
            disabled=True,
            required=False,
            help_text = 'Ensure you save this token somewhere as you will never be able to obtain it again',
        )
