from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_identifier.models import SubjectIdentifierManager
from edc_protocol.validators import datetime_not_before_study_start

from ...choices import CAUSE_OF_DEATH, TB_SITE_DEATH


class DeathReport(UniqueSubjectIdentifierFieldMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    death_datetime = models.DateTimeField(
        validators=[datetime_not_future],
        verbose_name='Date and Time of Death')

    study_day = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(80)],
        verbose_name='Study day')

    death_as_inpatient = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Death as inpatient')

    cause_of_death = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH,
        verbose_name='Main cause of death (opinion of local study Dr and '
                     'local PI)',
        help_text='Tick only 1:(NB. Fill in AE CRF)')

    cause_of_death_other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    tb_site = models.CharField(
        max_length=25,
        choices=TB_SITE_DEATH,
        blank=True,
        null=True,
        verbose_name='If cause of death is TB, specify site of TB disease')

    death_narrative = models.TextField(
        verbose_name='Narrative')

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier, )
