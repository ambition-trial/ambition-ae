from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_protocol.validators import datetime_not_before_study_start

from ...choices import CAUSE_OF_DEATH, TB_SITE_DEATH
from .death_report import DeathReport


class BaseDeathReportTmg(models.Model):

    death_report = models.OneToOneField(DeathReport, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    cause_of_death = models.CharField(
        verbose_name='Main cause of death (opinion of TMG member)',
        max_length=50,
        choices=CAUSE_OF_DEATH,
        help_text='Tick only 1:(NB. Fill in AE CRF)')

    cause_of_death_agreed = models.CharField(
        verbose_name='Cause of death agreed between study doctor and TMG member?',
        max_length=5,
        choices=YES_NO,
        help_text='If No, complete Q10 below')

    cause_of_death_other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    tb_site = models.CharField(
        verbose_name='If cause of death is TB, specify site of TB disease',
        max_length=25,
        choices=TB_SITE_DEATH,
        blank=True,
        null=True)

    death_narrative = models.TextField(
        verbose_name='Narrative')

    def __str__(self):
        return str(self.death_report)

    def natural_key(self):
        return self.death_report.natural_key()

    class Meta:
        abstract = True
