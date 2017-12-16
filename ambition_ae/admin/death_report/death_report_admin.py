from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ...admin_site import ambition_ae_admin
from ...forms import DeathReportForm
from ...models import DeathReport
from ..modeladmin_mixins import ModelAdminMixin


@admin.register(DeathReport, site=ambition_ae_admin)
class DeathReportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DeathReportForm

    radio_fields = {
        'death_as_inpatient': admin.VERTICAL,
        'cause_of_death': admin.VERTICAL,
        'tb_site': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'death_datetime',
                'study_day',
                'death_as_inpatient')},
         ),
        ('Opinion of Local Study Doctor', {
            'fields': (
                'cause_of_death',
                'cause_of_death_other',
                'tb_site')}),
        ('Summary', {
            'fields': (
                'death_narrative',)}),
        audit_fieldset_tuple
    )
