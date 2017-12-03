from django import forms

from ..models import AeFinal
from .modelform_mixin import ModelformMixin


class AeFinalForm(ModelformMixin, forms.ModelForm):

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = AeFinal
        fields = '__all__'
