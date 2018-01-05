from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.db.models.deletion import PROTECT
from django.urls.base import reverse
from django.utils.safestring import mark_safe
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_validators import date_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_constants.constants import YES, NOT_APPLICABLE, NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_identifier.model_mixins import TrackingIdentifierModelMixin

from ..action_items import AeFollowupAction
from ..admin_site import ambition_ae_admin
from ..choices import AE_OUTCOME, AE_GRADE_SIMPLE
from ..managers import AeManager
from .ae_initial import AeInitial


class AeFollowup(ActionItemModelMixin,
                 NonUniqueSubjectIdentifierFieldMixin,
                 TrackingIdentifierModelMixin, SiteModelMixin, BaseUuidModel):

    action_cls = AeFollowupAction
    tracking_identifier_prefix = 'AF'

    ae_initial = models.ForeignKey(AeInitial, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report date and time",
        default=get_utcnow)

    outcome = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        choices=AE_OUTCOME)

    outcome_date = models.DateField(
        validators=[date_not_future])

    # TODO: add validation against 'outcome'
    # if increased create TMG action
    ae_grade = models.CharField(
        verbose_name='If severity increased, indicate grade',
        max_length=25,
        choices=AE_GRADE_SIMPLE,
        default=NOT_APPLICABLE)

    relevant_history = models.TextField(
        verbose_name='Description summary of Adverse Event outcome',
        max_length=1000,
        blank=False,
        null=False,
        help_text='Indicate Adverse Event, clinical results,'
        'medications given, dosage,treatment plan and outcomes.')

    followup = models.CharField(
        verbose_name='Is a follow-up to this report required?',
        max_length=15,
        choices=YES_NO,
        default=YES,
        help_text='If NO, this will be considered the final report')

    objects = AeManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.ae_initial.subject_identifier
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.report_datetime, ) + self.ae_initial.natural_key()

    @property
    def next(self):
        if self.followup == YES:
            return 'AE Followup'
        elif self.followup == NO and self.ae_grade != NOT_APPLICABLE:
            return 'AE Initial'
        else:
            return 'Final'
        return self.followup

    @property
    def severity(self):
        if self.ae_grade == NOT_APPLICABLE:
            return 'unchanged'
        return self.ae_grade

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
    def action_item_reason(self):
        return self.ae_initial.ae_description

    class Meta:
        verbose_name = 'AE Follow-up Report'
