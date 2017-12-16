from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_ae_admin
from ..forms import AeTmgForm
from ..models import AeTmg
from .modeladmin_mixins import ModelAdminMixin, NonAeInitialModelAdminMixin


@admin.register(AeTmg, site=ambition_ae_admin)
class AeTmgAdmin(ModelAdminMixin, NonAeInitialModelAdminMixin, admin.ModelAdmin):

    form = AeTmgForm

    additional_instructions = 'For completion by TMG Investigator Only'

    list_display = ['ae_initial', 'subject_identifier', 'report_datetime',
                    'officials_notified', 'investigator_returned']

    search_fields = ['ae_initial__tracking_identifier',
                     'ae_initial__subject_identifier']

    fieldsets = (
        (None, {
            'fields': (
                'ae_initial',
                'report_datetime',
                'ae_received_datetime',
                'clinical_review_datetime',
                'investigator_comments',
                'ae_description',
                'ae_classification',
                'ae_classification_other',
                'officials_notified',
                'investigator_returned')}),
        ['Action', {'classes': ('collapse', ), 'fields': (
            'tracking_identifier', 'action_identifier')}],
        audit_fieldset_tuple
    )

    filter_horizontal = ('ae_classification',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj=obj)
        return fields + ('tracking_identifier', 'action_identifier')
