from django import forms

from ...form_validators import DeathReportFormValidator
from ...models import DeathReportTmgOne, DeathReportTmgTwo


class DeathReportTmgOneForm(forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReportTmgOne
        fields = '__all__'


class DeathReportTmgTwoForm(forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReportTmgTwo
        fields = '__all__'
