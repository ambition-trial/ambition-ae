from django import forms

from ..models import AeFollowup
from .modelform_mixin import ModelformMixin


class AeFollowupForm(ModelformMixin, forms.ModelForm):

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = AeFollowup
        fields = '__all__'
