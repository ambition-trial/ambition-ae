from django.db import models
from django.db.models.deletion import PROTECT
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_identifier.model_mixins import TrackingIdentifierModelMixin

from .ae_initial import AeInitial
from .managers import AeManager


class AeFinal(ActionItemModelMixin, TrackingIdentifierModelMixin,
              NonUniqueSubjectIdentifierFieldMixin, BaseUuidModel):

    ae_initial = models.OneToOneField(AeInitial, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow)

    relevant_history = models.TextField(
        verbose_name='Description Summary Of Adverse Event Outcome',
        max_length=1000,
        blank=False,
        null=False,
        help_text='Indicate Adverse Event, Clinical results,'
        'medications given, dosage,treatment plan and outcomes.')

    objects = AeManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.ae_initial.subject_identifier
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.report_datetime, ) + self.ae_initial.natural_key()

    class Meta:
        verbose_name = 'AE Final Report'
