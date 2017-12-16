from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel

from .base_death_report_tmg import BaseDeathReportTmg
from .managers import DeathReportTmgManager


class DeathReportTmgOne(BaseDeathReportTmg, BaseUuidModel):

    objects = DeathReportTmgManager()

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Death report TMG 1'


class DeathReportTmgTwo(BaseDeathReportTmg, BaseUuidModel):

    objects = DeathReportTmgManager()

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Death report TMG 2'
