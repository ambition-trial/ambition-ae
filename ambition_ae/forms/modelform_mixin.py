from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_registration.models import RegisteredSubject
from pprint import pprint


class ModelformMixin:

    action_identifier = forms.CharField(
        label='Action Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        cleaned_data = super().clean()
        subject_identifier = cleaned_data.get('subject_identifier')
        pprint(cleaned_data)
        try:
            RegisteredSubject.objects.get(
                subject_identifier=subject_identifier)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                {'subject_identifier': 'Invalid.'})
        return cleaned_data
