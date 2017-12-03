from django import forms

from ..models import AeTmg
from .modelform_mixin import ModelformMixin


class AeTmgForm(ModelformMixin, forms.ModelForm):

    class Meta:
        model = AeTmg
        fields = '__all__'
