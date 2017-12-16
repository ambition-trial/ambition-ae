from django import forms

from ..form_validators import ProtocolDeviationViolationFormValidator
from ..models import ProtocolDeviationViolation


class ProtocolDeviationViolationForm(forms.ModelForm):

    form_validator_cls = ProtocolDeviationViolationFormValidator

    class Meta:
        model = ProtocolDeviationViolation
        fields = '__all__'
