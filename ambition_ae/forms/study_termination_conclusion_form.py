from django import forms
from edc_offstudy.modelform_mixins import OffstudyNonCrfModelFormMixin
from ..models import StudyTerminationConclusion
from ..form_validators import StudyTerminationConclusionFormValidator


class StudyTerminationConclusionForm(OffstudyNonCrfModelFormMixin, forms.ModelForm):

    form_validator_cls = StudyTerminationConclusionFormValidator

    class Meta:
        model = StudyTerminationConclusion
        fields = '__all__'
        labels = {
            'offstudy_datetime': 'Date patient terminated on study:',
        }
