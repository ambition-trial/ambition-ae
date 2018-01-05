from django import forms
from edc_form_validators import FormValidatorMixin, FormValidator

from ..models import AeTmg
from .modelform_mixin import ModelformMixin
from edc_constants.constants import CLOSED


class AeTmgFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            CLOSED, field='report_status', field_required='report_closed_datetime')


class AeTmgForm(FormValidatorMixin, ModelformMixin, forms.ModelForm):

    form_validator_cls = AeTmgFormValidator

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = AeTmg
        fields = '__all__'
