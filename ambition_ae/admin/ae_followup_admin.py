from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_ae_admin
from ..forms import AeFollowupForm
from ..models import AeFollowup
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AeFollowup, site=ambition_ae_admin)
class AeFollowupAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AeFollowupForm

    fieldsets = (
        (None, {
            'fields': (
                'ae_initial',
                'action_identifier',
                'report_datetime',
                'outcome',
                'outcome_date',
                'relevant_history')},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {
        'outcome': admin.VERTICAL}

    search_fields = ['ae_initial__tracking_identifier',
                     'ae_initial__subject_identifier']
