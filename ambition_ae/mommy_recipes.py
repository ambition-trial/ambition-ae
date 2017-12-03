from edc_constants.constants import YES, NO
from faker import Faker
from model_mommy.recipe import Recipe

from .models import AeInitial, AeTmg, AeFollowup, AeFinal, AEClassification


fake = Faker()

aeclassification = Recipe(AEClassification)

aeinitial = Recipe(
    AeInitial,
    ae_study_relation_possibility=YES,
    ambisome_relation='not_related',
    fluconazole_relation='not_related',
    amphotericin_b_relation='not_related',
    ae_cause=NO,
    ae_cause_other=None)

aetmg = Recipe(AeTmg)

aefollowup = Recipe(
    AeFollowup,
    relevant_history=NO)

aefinal = Recipe(AeFinal)
