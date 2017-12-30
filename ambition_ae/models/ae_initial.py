from ambition_rando import SINGLE_DOSE, CONTROL, SINGLE_DOSE_NAME, CONTROL_NAME
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.utils.safestring import mark_safe
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel, SiteModelMixin
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO, YES_NO_NA, YES_NO_UNKNOWN
from edc_constants.constants import NOT_APPLICABLE, UNKNOWN
from edc_identifier.managers import TrackingIdentifierManager
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_identifier.model_mixins import TrackingIdentifierModelMixin

from ..action_items import AeInitialAction
from ..choices import STUDY_DRUG_RELATIONSHIP, SAE_REASONS
from ..model_mixins import AeModelMixin


class AeInitial(AeModelMixin, ActionItemModelMixin,
                TrackingIdentifierModelMixin, NonUniqueSubjectIdentifierFieldMixin,
                SiteModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'AE'

    action_cls = AeInitialAction

    ae_name = models.CharField(
        verbose_name=('Short description of AE'),
        max_length=25,
        blank=False,
        null=True)

    # TODO: Get this from the Randomization
    regimen = models.CharField(
        verbose_name='Patient’s treatment regimen',
        max_length=50,
        choices=(
            (SINGLE_DOSE, 'Single dose'),
            (CONTROL, 'Control'),
        ),
        help_text=mark_safe(
            f'<ul><li>{SINGLE_DOSE_NAME}<li>{CONTROL_NAME}</ul>'))

    ae_study_relation_possibility = models.CharField(
        verbose_name=(
            'Is the incident related to the patient involvement in the study?'),
        max_length=10,
        choices=YES_NO_UNKNOWN)

    ambisome_relation = models.CharField(
        verbose_name='Relationship to Ambisome:',
        max_length=25,
        choices=STUDY_DRUG_RELATIONSHIP)

    fluconazole_relation = models.CharField(
        verbose_name='Relationship to Fluconozole:',
        max_length=25,
        choices=STUDY_DRUG_RELATIONSHIP)

    amphotericin_b_relation = models.CharField(
        verbose_name='Relationship to Amphotericin B:',
        max_length=25,
        choices=STUDY_DRUG_RELATIONSHIP)

    flucytosine_relation = models.CharField(
        verbose_name='Relationship to Flucytosine:',
        max_length=25,
        choices=STUDY_DRUG_RELATIONSHIP)

    details_last_study_drug = models.TextField(
        verbose_name='Details of the last implicated drug (name, dose, route):',
        max_length=1000,
        null=True,
        blank=True)

    med_administered_datetime = models.DateTimeField(
        verbose_name='Date and time of last implicated study medication administered',
        validators=[datetime_not_future],
        null=True,
        blank=True)

    ae_cause = models.CharField(
        verbose_name=('Has a reason other than the specified study drug been '
                      'identified as the cause of the event(s)?'),
        choices=YES_NO,
        max_length=5)

    ae_cause_other = OtherCharField(
        verbose_name='If YES, specify',
        max_length=250,
        blank=True,
        null=True)

    ae_treatment = models.TextField(
        verbose_name='Specify action taken for treatment of AE:')

    # TODO: If yes Use rule group to open recurrence form
    ae_cm_recurrence = models.CharField(
        verbose_name='Was the AE a recurrence of CM symptoms?',
        max_length=10,
        choices=YES_NO,
        default=UNKNOWN,
        help_text='If YES, fill in the "Recurrence of Symptoms" form')

    sae = models.CharField(
        verbose_name='Is this event a SAE?',
        max_length=5,
        choices=YES_NO,
        help_text=('(i.e. results in death, in-patient '
                   'hospitalisation/prolongation, significant disability or is '
                   'life-threatening)'))

    sae_reason = models.CharField(
        verbose_name='If YES, reason for SAE:',
        max_length=50,
        choices=SAE_REASONS,
        default=NOT_APPLICABLE)

    susar = models.CharField(
        verbose_name=(
            'Is this a Suspected Unexpected Serious Adverse Reaction (SUSAR)?'),
        choices=YES_NO,
        max_length=5,
        help_text=('If yes, SUSAR must be reported to Principal '
                   'Investigator and TMG immediately,'))

    susar_reported = models.CharField(
        verbose_name='Is SUSAR reported?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    tmg_report_datetime = models.DateTimeField(
        verbose_name='Date and time AE reported to TMG',
        blank=True,
        null=True,
        help_text=(
            'AEs ≥ Grade 4 or SAE must be reported to the Trial '
            'Management Group (TMG) within 24 hours'))

    objects = TrackingIdentifierManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    def __str__(self):
        return f'{self.tracking_identifier[-9:]} Grade {self.ae_grade}'

    @property
    def action_item_reason(self):
        return self.ae_description

    @property
    def description(self):
        """Returns a description.
        """
        return f'{self.tracking_identifier[-9:]} Grade-{self.ae_grade}. {self.ae_description}'

    class Meta:
        verbose_name = 'AE Initial Report'
