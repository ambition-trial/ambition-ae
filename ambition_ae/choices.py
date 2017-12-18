from edc_constants.constants import NOT_APPLICABLE, OTHER, YES, NO

from .constants import GRADE3, GRADE4, GRADE5, MILD, MODERATE, SEVERE

AE_INTENSITY = (
    (MILD, 'Mild'),
    (MODERATE, 'Moderate'),
    (SEVERE, 'Severe')
)

AE_REPORT_TYPE = (
    ('initial', 'Initial'),
    ('follow_up', 'Follow Up'),
    ('final', 'Final')
)

AE_GRADE = (
    (GRADE3, 'Grade III - Severe'),
    (GRADE4, 'Grade 4 - Life-threatening'),
    (GRADE5, 'Grade 5 - Death'),
)

AE_GRADE_SIMPLE = (
    (GRADE4, 'Grade 4 - Life-threatening'),
    (GRADE5, 'Grade 5 - Death'),
)

# TODO: validate Severity increased from Grade III
AE_OUTCOME = (
    ('continuing/update', 'Continuing/Update'),
    ('increase_from_g3', 'Severity increased from Grade III'),
    ('recovered', 'Recovered/Resolved'),
    ('recovering', 'Recovering/Resolving at end of study'),
    ('not_recovered', 'Not Recovered/Resolved at end of study'),
    ('unknown', 'Unknown/Lost to follow-up'),
    ('recovered_with_sequelae', 'Recovered with sequelae'),
    ('death', 'Death'),
)


DR_OPINION = (
    ('cm_release', 'CM Relapse'),
    ('cm_iris', 'CM IRIS'),
    (OTHER, 'Other'),
)

SAE_REASONS = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('death', 'Death (Please complete Death form and Study termination form)'),
    ('life_threatening', 'Life-threatening'),
    ('significant_disability', 'Significant disability'),
    ('in-patient_hospitalization',
     'In-patient hospitalization or prolongation '
     '(beyond 1 week from study inclusion)'),
    ('medically_important_event',
     'Medically important event (e.g. Severe thrombophlebitis, Bacteraemia, '
     'recurrence of symptoms not requiring admission, Hospital acquired '
     'pneumonia)'),
)


STEROIDS_CHOICES = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('oral_prednisolone', 'Oral Prednisolone'),
    ('iv_dexamethasone', 'IV Dexamethasone used'),
    (OTHER, 'Other'),
)

STUDY_DRUG_RELATIONSHIP = (
    ('not_related', 'Not related'),
    ('possibly_related', 'Possibly related'),
    ('probably_related', 'Probably related'),
    ('definitely_related', 'Definitely related'),
    ('unlikely_related', 'Unlikely related'),
    (NOT_APPLICABLE, 'Not Applicable'),
)


YES_NO_ALREADY_ARV = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('on_arvs_before_enrollment', 'Already on ARVs before enrollment')
)
