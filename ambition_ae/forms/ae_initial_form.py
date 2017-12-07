from django import forms

from ambition_validators import AdverseEventFormValidator

from edc_form_validators import FormValidatorMixin

from ..models import AeInitial
from .modelform_mixin import ModelformMixin


class AeInitialForm(FormValidatorMixin, ModelformMixin, forms.ModelForm):

    form_validator_cls = AdverseEventFormValidator

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = AeInitial
        fields = '__all__'
