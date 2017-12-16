from django.contrib import admin
from edc_action_item import action_fieldset
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_ae_admin
from ..forms import ProtocolDeviationViolationForm
from ..models import ProtocolDeviationViolation
from .modeladmin_mixins import ModelAdminMixin


@admin.register(ProtocolDeviationViolation, site=ambition_ae_admin)
class ProtocolDeviationViolationAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ProtocolDeviationViolationForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'report_datetime',
            )}
         ),
        ('Assessment to confirm violation', {
            'fields': (
                'deviation_or_violation',
                'participant_safety_impact',
                'participant_safety_impact_details',
                'study_outcomes_impact',
                'study_outcomes_impact_details')},
         ),
        ('Details of violation', {
            'fields': (
                'date_violation_datetime',
                'protocol_violation_type',
                'protocol_violation_type_other',
                'violation_description',
                'violation_reason')}
         ),
        ('Actions taken', {
            'fields': (
                'corrective_action_datetime',
                'corrective_action',
                'preventative_action_datetime',
                'preventative_action',
                'action_required',)}),
        action_fieldset,
        audit_fieldset_tuple,
    )

    radio_fields = {
        'deviation_or_violation': admin.VERTICAL,
        'participant_safety_impact': admin.VERTICAL,
        'study_outcomes_impact': admin.VERTICAL,
        'protocol_violation_type': admin.VERTICAL,
        'action_required': admin.VERTICAL}

    list_display = ('subject_identifier', 'dashboard',
                    'report_datetime', 'action_required', 'deviation_or_violation',
                    'tracking_identifier', 'action_identifier')

    list_filter = ('action_required',
                   'deviation_or_violation')

    search_fields = ('tracking_identifier',
                     'subject_identifier', 'action_identifier')

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = ('tracking_identifier', ) + fields
        return fields
