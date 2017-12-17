from edc_constants.constants import YES, NO, OTHER
from faker import Faker
from model_mommy.recipe import Recipe

from .constants import GRADE4, MODERATE
from .models import AeInitial, AeTmg, AeFollowup, DeathReport, StudyTerminationConclusion
from .models import ProtocolDeviationViolation, RecurrenceSymptom, Neurological
from .models import MeningitisSymptom

fake = Faker()

aeinitial = Recipe(
    AeInitial,
    ae_description='A description of this event',
    ae_grade=GRADE4,
    ae_intensity=MODERATE,
    ae_study_relation_possibility=YES,
    ambisome_relation='not_related',
    fluconazole_relation='not_related',
    amphotericin_b_relation='not_related',
    ae_treatment='Some special treatment',
    ae_cm_recurrence=NO,
    sae=NO,
    susar=NO,
    ae_cause=NO,
    ae_cause_other=None)

aetmg = Recipe(AeTmg)

aefollowup = Recipe(
    AeFollowup,
    relevant_history=NO)

deathreport = Recipe(
    DeathReport,
    study_day=1,
    death_as_inpatient=YES,
    cause_of_death_study_doctor_opinion='art_toxicity',
    cause_other_study_doctor_opinion='None',
    cause_tb_study_doctor_opinion=None,
    cause_of_death_tmg1_opinion='art_toxicity',
    cause_other_tmg1_opinion='None',
    cause_tb_tmg1_opinion=None,
    cause_of_death_tmg2_opinion='art_toxicity',
    cause_other_tmg2_opinion='None',
    cause_tb_tmg2_opinion=None,
    narrative_summary=(
        'adverse event resulted in death due to cryptococcal meningitis'))

studyterminationconclusion = Recipe(StudyTerminationConclusion)

protocoldeviationviolation = Recipe(ProtocolDeviationViolation)

recurrencesymptom = Recipe(RecurrenceSymptom)

meningitissymptom = Recipe(
    MeningitisSymptom,
    name=OTHER,
    short_name='Other'
)

neurological = Recipe(
    Neurological,
    name='meningismus',
    short_name='Meningismus'
)
