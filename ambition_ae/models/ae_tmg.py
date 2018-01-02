from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.db.models.deletion import PROTECT
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_validators import date_not_future
from edc_base.utils import get_utcnow
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_identifier.model_mixins import TrackingIdentifierModelMixin

from ..action_items import AeTmgAction
from ..managers import AeManager
from .list_models import AeClassification
from .ae_initial import AeInitial


class AeTmg(ActionItemModelMixin, TrackingIdentifierModelMixin,
            NonUniqueSubjectIdentifierFieldMixin, SiteModelMixin, BaseUuidModel):

    action_cls = AeTmgAction
    tracking_identifier_prefix = 'AT'

    ae_initial = models.OneToOneField(AeInitial, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report date and time",
        default=get_utcnow)

    ae_received_datetime = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='Date and time AE form received:')

    clinical_review_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Date and time of clinical review: ')

    investigator_comments = models.TextField(
        blank=True,
        null=True,
        verbose_name='Investigator comments:')

    ae_classification = models.ManyToManyField(
        AeClassification,
        blank=True,
        verbose_name='Classification of AE:')

    ae_classification_other = OtherCharField(
        max_length=250,
        blank=True,
        null=True)

    ae_description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description of AE:')

    officials_notified = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='Date and time regulatory authorities notified (SUSARs)')

    investigator_returned = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name=('Date and time form logged in data base and returned'
                      'to Local Investigator'))

    objects = AeManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.ae_initial.subject_identifier
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.report_datetime, ) + self.ae_initial.natural_key()

    @property
    def action_item_reason(self):
        return self.ae_initial.ae_description

    class Meta:
        verbose_name = 'AE TMG Report'
