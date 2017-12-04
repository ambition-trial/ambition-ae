from django.conf import settings
from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO, YES_NO_NA, YES_NO_UNKNOWN
from edc_constants.constants import NOT_APPLICABLE, UNKNOWN
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_identifier.model_mixins import TrackingIdentifierModelMixin

from ..choices import STUDY_DRUG_RELATIONSHIP, SAE_REASONS
from ..model_mixins import AeInitialActionItemModelMixin, AeModelMixin
from ..managers import AeInitialManager


class AeInitial(AeModelMixin, AeInitialActionItemModelMixin,
                TrackingIdentifierModelMixin, NonUniqueSubjectIdentifierFieldMixin,
                BaseUuidModel):

    tracking_identifier_prefix = 'AE'

    # TODO: Get this from the Randomization
    regimen = models.CharField(
        verbose_name='Patient’s treatment regimen',
        max_length=50,
        help_text='Control: (Amphotericin B 1 mg/kg for 7 days with '
        'flucytosine 100mg/kg/day for 7 days followed by fluconazole '
        '1200mg/day for 7 days)')

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
        verbose_name='Date and time of last implicated study medication '
                     'administered',
        validators=[datetime_not_future],
        null=True,
        blank=True)

    ae_cause = models.CharField(
        verbose_name='Has a reason other than the specified study drug been '
                     ' identified as the cause of the event(s)?',
        choices=YES_NO,
        max_length=5)

    ae_cause_other = OtherCharField(
        verbose_name='If yes, specify',
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
        help_text='If yes, fill in the Recurrence of Symptoms form')

    sae = models.CharField(
        verbose_name='Is this event a SAE?',
        max_length=5,
        choices=YES_NO,
        help_text='(i.e. results in death, in-patient '
                  'hospitalisation/prolongation, significant disability or is '
                  'life-threatening)')

    sae_reason = models.CharField(
        verbose_name='If Yes, Reason for SAE:',
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
            'Management Group (TMG) within 48hrs (Email to: '
            f'{settings.EMAIL_CONTACTS.get("ae_reports")}'))

    objects = AeInitialManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.tracking_identifier[-9:]} Grade {self.ae_grade}'

    @property
    def description(self):
        """Returns a description.
        """
        return f'{self.tracking_identifier[-9:]} Grade-{self.ae_grade}. {self.ae_description}'

    class Meta:
        verbose_name = 'AE Initial Report'
