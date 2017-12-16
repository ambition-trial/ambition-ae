from django import forms

from ..models import StudyTerminationConclusion
from ..form_validators import StudyTerminationConclusionFormValidator


class StudyTerminationConclusionForm(forms.ModelForm):

    form_validator_cls = StudyTerminationConclusionFormValidator

    class Meta:
        model = StudyTerminationConclusion
        fields = '__all__'
