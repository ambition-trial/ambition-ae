from django import forms
from edc_form_validators import FormValidatorMixin, FormValidator

from ..constants import SEVERITY_INCREASED_FROM_G3
from ..models import AeFollowup
from .modelform_mixin import ModelformMixin


class AeFollowupFormValidator(FormValidator):

    def clean(self):

        self.applicable_if(
            SEVERITY_INCREASED_FROM_G3,
            field='outcome', field_applicable='ae_grade')


class AeFollowupForm(FormValidatorMixin, ModelformMixin, forms.ModelForm):

    form_validator_cls = AeFollowupFormValidator

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = AeFollowup
        fields = '__all__'
