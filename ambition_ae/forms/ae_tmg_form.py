from django import forms
from edc_action_item.forms import ActionItemFormMixin
from edc_form_validators import FormValidatorMixin

from ..form_validators import AeTmgFormValidator
from ..models import AeTmg
from .modelform_mixin import ModelFormMixin


class AeTmgForm(
    FormValidatorMixin, ModelFormMixin, ActionItemFormMixin, forms.ModelForm
):

    form_validator_cls = AeTmgFormValidator

    subject_identifier = forms.CharField(
        label="Subject Identifier",
        required=False,
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )

    ae_description = forms.CharField(
        label="Original AE Description",
        required=False,
        widget=forms.Textarea(attrs={"readonly": "readonly", "cols": "79"}),
    )

    ae_classification = forms.CharField(
        label="AE Classification",
        required=False,
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )

    class Meta:
        model = AeTmg
        fields = "__all__"
