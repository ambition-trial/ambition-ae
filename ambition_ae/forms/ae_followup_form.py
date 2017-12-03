from django import forms

from ..models import AeFollowup
from .modelform_mixin import ModelformMixin


class AeFollowupForm(ModelformMixin, forms.ModelForm):

    class Meta:
        model = AeFollowup
        fields = '__all__'
