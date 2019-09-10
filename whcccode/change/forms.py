from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from change.models import Change


class ChangeForm(forms.ModelForm):
    class Meta:
        model = Change
        fields = ('initial_value',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Make Change'))