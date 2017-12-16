from django import forms

from ...form_validators import DeathReportFormValidator
from ...models import DeathReport


class DeathReportForm(forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReport
        fields = '__all__'
