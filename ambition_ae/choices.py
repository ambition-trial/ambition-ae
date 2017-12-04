from edc_constants.constants import NOT_APPLICABLE
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
    (GRADE3, 'Grade 3'),
    (GRADE4, 'Grade 4 - Life-threatening'),
    (GRADE5, 'Grade 5 - Death'),
)

AE_OUTCOME = (
    ('recovered', 'Recovered/Resolved'),
    ('recovering', 'Recovering/Resolving at end of study'),
    ('not_recovered', 'Not Recovered/Resolved at end of study'),
    ('unknown', 'Unknown/Lost to follow-up'),
    ('recovered_with_sequelae', 'Recovered with sequelae'),
    ('Death', 'Death'),
)

SAE_REASONS = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('death', 'Death (Please complete Death form and Study termination form)'),
    ('life_threatening', 'Life-threatening'),
    ('significant_disability', 'Significant disability'),
    ('in-patient_hospitalization or prolongation',
     'In-patient hospitalization or prolongation '
     '(beyond 1 week from study inclusion)'),
    ('Medically_important_event',
     'Medically important event (e.g. Severe thrombophlebitis, Bacteraemia, '
     'recurrence of symptoms not requiring admission, Hospital acquired '
     'pneumonia)'),
)


STUDY_DRUG_RELATIONSHIP = (
    ('not_related', 'Not related'),
    ('possibly_related', 'Possibly related'),
    ('probably_related', 'Probably related'),
    ('definitely_related', 'Definitely related'),
    ('unlikely_related', 'Unlikely related'),
    (NOT_APPLICABLE, 'Not Applicable'),
)
