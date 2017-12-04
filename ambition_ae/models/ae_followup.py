from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_validators import date_not_future
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_constants.choices import YES_NO
from edc_constants.constants import YES
from edc_identifier.model_mixins import TrackingIdentifierModelMixin

from ..choices import AE_OUTCOME
from ..managers import AeManager
from ..model_mixins import AeFollowupActionItemModelMixin
from .ae_initial import AeInitial


class AeFollowup(AeFollowupActionItemModelMixin,
                 NonUniqueSubjectIdentifierFieldMixin,
                 TrackingIdentifierModelMixin, BaseUuidModel):

    ae_initial = models.ForeignKey(AeInitial, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow)

    outcome = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        choices=AE_OUTCOME)

    outcome_date = models.DateField(
        validators=[date_not_future],
        help_text='Date of Outcome')

    relevant_history = models.TextField(
        verbose_name='Description Summary Of Adverse Event Outcome',
        max_length=1000,
        blank=False,
        null=False,
        help_text='Indicate Adverse Event, Clinical results,'
        'medications given, dosage,treatment plan and outcomes.')

    followup = models.CharField(
        verbose_name='Is a follow-up to this report required?',
        max_length=15,
        choices=YES_NO,
        default=YES,
        help_text='If NO, this will be considered the final report')

    objects = AeManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.ae_initial.subject_identifier
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.report_datetime, ) + self.ae_initial.natural_key()

    class Meta:
        verbose_name = 'AE Follow-up Report'
