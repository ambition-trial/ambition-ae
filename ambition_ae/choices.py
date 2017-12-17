from edc_constants.constants import NOT_APPLICABLE, OTHER, UNKNOWN, YES, NO,\
    DEAD

from .constants import AZT_3TC_with_ATZ_r_or_Lopinavir_r
from .constants import AZT_3TC_with_EFV_NVP_or_DTG
from .constants import GRADE3, GRADE4, GRADE5, MILD, MODERATE, SEVERE
from .constants import TDF_3TC_FTC_with_ATZ_r_or_Lopinavir_r
from .constants import TDF_3TC_FTC_with_EFV_or_NVP
from .constants import TUBERCULOSIS, DEVIATION, VIOLATION, CONSENT_WITHDRAWAL

ACTION_REQUIRED = (
    ('remain_on_study', 'Participant to remain on trial'),
    ('to_be_withdrawn', 'Participant to be withdrawn from trial'),
    ('remain_on_study_modified',
     'Patient remains on study but data analysis will be modified')
)

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

CAUSE_OF_DEATH = (
    ('cryptococcal_meningitis', 'Cryptococcal meningitis'),
    ('Cryptococcal_meningitis_relapse_IRIS',
     'Cryptococcal meningitis relapse/IRIS'),
    (TUBERCULOSIS, 'TB'),
    ('bacteraemia', 'Bacteraemia'),
    ('bacterial_pneumonia', 'Bacterial pneumonia'),
    ('malignancy', 'Malignancy'),
    ('art_toxicity', 'ART toxicity'),
    ('IRIS_non_CM', 'IRIS non-CM'),
    ('diarrhea_wasting', 'Diarrhea/wasting'),
    (UNKNOWN, 'Unknown'),
    (OTHER, 'Other'),
)


DEVIATION_VIOLATION = (
    (DEVIATION, 'Deviation'),
    (VIOLATION, 'Violation'),
)

DR_OPINION = (
    ('cm_release', 'CM Relapse'),
    ('cm_iris', 'CM IRIS'),
    (OTHER, 'Other'),
)

FIRST_ARV_REGIMEN = (
    (NOT_APPLICABLE, 'Not applicable'),
    (TDF_3TC_FTC_with_EFV_or_NVP,
     'TDF + 3TC/FTC + either EFV or NVP or DTG'),
    (AZT_3TC_with_EFV_NVP_or_DTG,
     'AZT+3TC+ either EFV or NVP or DTG'),
    (OTHER, 'Other'),
)

FIRST_LINE_REGIMEN = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('EFV', 'EFV'),
    ('DTG', 'DTG'),
    ('NVP', 'NVP'),
)

REASON_STUDY_TERMINATED = (
    ('10_weeks_completed_follow_up', 'Patient completed 10 weeks of follow-up'),
    ('patient_lost_to_follow_up', 'Patient lost to follow-up'),
    ('dead', 'Reported/known to have died'),
    (CONSENT_WITHDRAWAL, 'Withdrawal of Subject Consent for '
     'participation'),
    ('care_transferred_to_another_institution',
     'Care transferred to another institution'),
    ('late_exclusion_criteria_met', 'Late exclusion criteria met'),
    ('included_in_error', 'Included in error'),
)

SECOND_ARV_REGIMEN = (
    (NOT_APPLICABLE, 'Not applicable'),
    (TDF_3TC_FTC_with_ATZ_r_or_Lopinavir_r,
     'TDF + 3TC/FTC + either ATZ/r or Lopinavir/r'),
    (AZT_3TC_with_ATZ_r_or_Lopinavir_r,
     'AZT +3TC + either ATZ/r or Lopinavir/r'),
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

PROTOCOL_VIOLATION = (
    ('failure_to_obtain_informed_consent', 'Failure to obtain informed '
     'consent'),
    ('enrollment_of_ineligible_patient', 'Enrollment of ineligible patient'),
    ('screening_procedure not done', 'Screening procedure required by '
     'protocol not done'),
    ('screening_or_on-study_procedure', 'Screening or on-study procedure/lab '
     'work required not done'),
    ('incorrect_research_treatment', 'Incorrect research treatment given to '
     'patient'),
    ('procedure_not_completed', 'On-study procedure required by protocol not '
     'completed'),
    ('visit_non-compliance', 'Visit non-compliance'),
    ('medication_stopped_early', 'Medication stopped early'),
    ('medication_noncompliance', 'Medication_noncompliance'),
    ('national_regulations_not_met', 'Standard WPD, ICH-GCP, local/national '
     'regulations not met'),
    (OTHER, 'Other'),
)

REASON_STUDY_TERMINATED = (
    ('10_weeks_completed_follow_up',
     'Patient completed 10 weeks of follow-up'),
    ('patient_lost_to_follow_up', 'Patient lost to follow-up'),
    (DEAD, 'Reported/known to have died'),
    (CONSENT_WITHDRAWAL, 'Withdrawal of Subject Consent for '
     'participation'),
    ('care_transferred_to_another_institution',
     'Care transferred to another institution'),
    ('late_exclusion_criteria_met', 'Late exclusion criteria met'),
    ('included_in_error', 'Included in error'),
)
TB_SITE_DEATH = (
    ('meningitis', 'Meningitis'),
    ('pulmonary', 'Pulmonary'),
    ('disseminated', 'Disseminated'),
)

YES_NO_ALREADY_ARV = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('on_arvs_before_enrollment', 'Already on ARVs before enrollment')
)

YES_NO_ALREADY = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('already_on_rifampicin', 'Already on Rifampicin'),
)
