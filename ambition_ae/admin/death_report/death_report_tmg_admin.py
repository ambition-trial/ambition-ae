from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ...admin_site import ambition_ae_admin
from ...forms import DeathReportTmgOneForm, DeathReportTmgTwoForm
from ...models import DeathReportTmgOne, DeathReportTmgTwo
from ..modeladmin_mixins import ModelAdminMixin


class DeathReportTmgModelAdminMixin(ModelAdminMixin):

    fieldsets = (
        ('Opinion of TMG', {
            'fields': (
                'death_report',
                'cause_of_death',
                'cause_of_death_other',
                'tb_site',
                'cause_of_death_agreed')}),
        ('Summary', {
            'fields': (
                'death_narrative',)}),
        audit_fieldset_tuple
    )

    radio_fields = {
        'cause_of_death': admin.VERTICAL,
        'cause_of_death_agreed': admin.VERTICAL,
        'tb_site': admin.VERTICAL}


@admin.register(DeathReportTmgOne, site=ambition_ae_admin)
class DeathReportTmgOneAdmin(DeathReportTmgModelAdminMixin, admin.ModelAdmin):

    form = DeathReportTmgOneForm


@admin.register(DeathReportTmgTwo, site=ambition_ae_admin)
class DeathReportTmgTwoAdmin(DeathReportTmgModelAdminMixin, admin.ModelAdmin):

    form = DeathReportTmgTwoForm
