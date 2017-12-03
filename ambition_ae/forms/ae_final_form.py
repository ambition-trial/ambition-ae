from django import forms

from ..models import AeFinal
from .modelform_mixin import ModelformMixin


class AeFinalForm(ModelformMixin, forms.ModelForm):

    class Meta:
        model = AeFinal
        fields = '__all__'
