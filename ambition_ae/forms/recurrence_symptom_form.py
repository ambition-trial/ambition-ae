from django import forms

from ..form_validators import RecurrenceSymptomFormValidator
from ..models import RecurrenceSymptom
from .modelform_mixin import ModelformMixin


class RecurrenceSymptomForm(ModelformMixin, forms.ModelForm):

    form_validator_cls = RecurrenceSymptomFormValidator

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = RecurrenceSymptom
        fields = '__all__'
