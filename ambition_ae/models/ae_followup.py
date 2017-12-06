from django.db import models
from django.db.models.deletion import PROTECT
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_base.model_validators import date_not_future
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_constants.choices import YES_NO
from edc_constants.constants import YES
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from django.urls.base import reverse
from django.utils.safestring import mark_safe

from ..action_items import AeFollowupAction
from ..admin_site import ambition_ae_admin
from ..choices import AE_OUTCOME
from ..managers import AeManager
from .ae_initial import AeInitial


class AeFollowup(ActionItemModelMixin,
                 NonUniqueSubjectIdentifierFieldMixin,
                 TrackingIdentifierModelMixin, BaseUuidModel):

    action_cls = AeFollowupAction

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
        validators=[date_not_future])

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

    @property
    def initial(self):
        """Returns a shortened action identifier.
        """
        if self.ae_initial:
            url_name = '_'.join(self._meta.label_lower.split('.'))
            namespace = ambition_ae_admin.name
            url = reverse(
                f'{namespace}:{url_name}_changelist')
            return mark_safe(
                f'<a data-toggle="tooltip" title="go to ae initial report" '
                f'href="{url}?q={self.ae_initial.tracking_identifier}">'
                f'{self.ae_initial.identifier}</a>')
        return None

    @property
    def parent_action_reason(self):
        return self.ae_initial.ae_description

    class Meta:
        verbose_name = 'AE Follow-up Report'
