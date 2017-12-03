from django.contrib import admin
# from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_ae_admin
from ..forms import AeFinalForm
from ..models import AeFinal
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AeFinal, site=ambition_ae_admin)
class AeFinalAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AeFinalForm

#     fieldsets = (
#         (None, {
#             'fields': (
#                 'adverse_event',
#                 'report_datetime',
#                 'outcome',
#                 'outcome_date',
#                 'relevant_history')},
#          ),
#         audit_fieldset_tuple
#     )
#
#     radio_fields = {
#         'outcome': admin.VERTICAL}
#
#     search_fields = ['adverse_event__tracking_identifier',
#                      'adverse_event__subject_identifier']
