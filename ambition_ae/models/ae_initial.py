from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_action_item.models import ActionItem
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future, datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO, YES_NO_NA, YES_NO_UNKNOWN
from edc_constants.constants import NOT_APPLICABLE, UNKNOWN, YES
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_identifier.model_mixins import TrackingIdentifierModelMixin

from ..choices import AE_GRADE, AE_INTENSITY, RAE_REASON
from ..choices import STUDY_DRUG_RELATIONSHIP
from .managers import AeInitialManager


class AeInitialActionItemModelMixin(ActionItemModelMixin):

    def creates_action_items(self):
        action_items = ['submit-initial-ae-report']
        return action_items

    def create_next_action_items(self, action_type_name=None):
        action_items = []
        if action_type_name:
            action_items.append(action_type_name)
        try:
            ActionItem.objects.get(
                subject_identifier=self.subject_identifier,
                parent_reference_identifier=self.tracking_identifier,
                reference_model='ambition_ae.aetmg')
        except ObjectDoesNotExist:
            action_items.append('submit-ae-tmg-report')
        if self.ae_cm_recurrence == YES:
            action_items.append('submit-recurrence-symptoms')
        return action_items

    class Meta:
        abstract = True


class AeModelMixin(models.Model):

    ae_auto_created = models.BooleanField(
        max_length=25,
        default=False,
        editable=False)

    ae_auto_created_criteria = models.CharField(
        max_length=50,
        default=NOT_APPLICABLE,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow)

    ae_description = models.TextField(
        verbose_name='Adverse Event (AE) description')

    ae_awareness_date = models.DateField(
        verbose_name='AE Awareness date',
        default=timezone.now,
        validators=[date_not_future])

    ae_start_date = models.DateField(
        verbose_name='Actual Start Date of AE',
        default=timezone.now,
        validators=[date_not_future])

    ae_grade = models.CharField(
        verbose_name='Severity of AE',
        max_length=25,
        choices=AE_GRADE)

    ae_intensity = models.CharField(
        verbose_name='What is the intensity AE',
        max_length=25,
        choices=AE_INTENSITY)

    class Meta:
        abstract = True


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
        choices=RAE_REASON,
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
