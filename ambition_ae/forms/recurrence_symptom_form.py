from django import forms

from ..form_validators import RecurrenceSymptomFormValidator
from ..models import RecurrenceSymptom


class RecurrenceSymptomForm(forms.ModelForm):

    form_validator_cls = RecurrenceSymptomFormValidator

    class Meta:
        model = RecurrenceSymptom
        fields = '__all__'
