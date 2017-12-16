from ambition_rando.models import RandomizationList
from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import AeInitialFormValidator
from ..models import AeInitial
from .modelform_mixin import ModelformMixin
from ambition_rando.constants import SINGLE_DOSE, SINGLE_DOSE_NAME, CONTROL,\
    CONTROL_NAME


class AeInitialForm(FormValidatorMixin, ModelformMixin, forms.ModelForm):

    form_validator_cls = AeInitialFormValidator

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def __init__(self, *args, **kwargs):
        self.drug_assignment = None
        initial = kwargs.get('initial', {})
        if initial.get('subject_identifier'):
            # set initial value of field regimen
            kwargs['initial'].update(
                regimen=self.get_drug_assignment(initial['subject_identifier']))
        super().__init__(*args, **kwargs)

    def get_drug_assignment(self, subject_identifier=None):
        obj = RandomizationList.objects.get(
            subject_identifier=subject_identifier)
        drug_assignment = obj.drug_assignment
        return drug_assignment

    def clean(self):
        cleaned_data = super().clean()
        drug_assignment = self.get_drug_assignment(
            cleaned_data.get('subject_identifier'))
        if cleaned_data.get('regimen') != drug_assignment:
            raise forms.ValidationError({
                'regimen':
                f'Incorrect. Subject was allocated to the '
                f'\'{drug_assignment.replace("_", " ")}\' arm.'})

    class Meta:
        model = AeInitial
        fields = '__all__'
