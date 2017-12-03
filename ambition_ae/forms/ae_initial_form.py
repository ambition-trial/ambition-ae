from django import forms

from ..models import AeInitial
from .modelform_mixin import ModelformMixin


class AeInitialForm(ModelformMixin, forms.ModelForm):

    class Meta:
        model = AeInitial
        fields = '__all__'
