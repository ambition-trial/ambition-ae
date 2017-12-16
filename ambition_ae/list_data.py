from edc_list_data import PreloadData
from edc_constants.constants import OTHER


list_data = {
    'ambition_ae.aeclassification': [
        ('anaemia', 'Anaemia'),
        ('thrombocytopenia', 'Thrombocytopenia'),
        ('diarrhoea', 'Diarrhoea'),
        ('thrombophlebitis', 'Renal impairment'),
        ('pneumonia', 'Pneumonia'),
        ('TB', 'TB'),
        ('hypokalaemia', 'Hypokalaemia'),
        ('bacteraemia/sepsis', 'Bacteraemia/Sepsis'),
        ('neutropaenia', 'Neutropaenia'),
        ('CM_IRIS', 'CM IRIS'),
        ('respiratory_distress', 'Respiratory distress'),
        (OTHER, 'Other')
    ],
    'ambition_ae.antibiotictreatment': [
        ('amoxicillin', 'Amoxicillin'),
        ('flucloxacillin', 'Flucloxacillin'),
        ('doxycycline', 'Doxycycline'),
        ('ceftriaxone', 'Ceftriaxone'),
        ('erythromycin', 'Erythromycin'),
        ('ciprofloxacin', 'Ciprofloxacin'),
        (OTHER, 'Other, specify')
    ],
    'ambition_ae.meningitissymptom': [
        ('headache', 'Headache'),
        ('vomiting', 'Vomiting'),
        ('fever', 'Fever'),
        ('seizures', 'Seizures'),
        ('neck_pain', 'Neck pain'),
        (OTHER, 'Other, specify')
    ],
    'ambition_ae.neurological': [
        ('meningism', 'Meningism'),
        ('papilloedema', ' Papilloedema'),
        ('focal_neurologic_deficit', 'Focal neurologic deficit'),
        ('CN_VI_palsy', 'Cranial Nerve VI palsy'),
        ('CN_III_palsy', 'Cranial Nerve III palsy'),
        ('CN_IV_palsy', 'Cranial Nerve IV palsy'),
        ('CN_VII_palsy', 'Cranial Nerve VII palsy'),
        ('CN_VIII_palsy', 'Cranial Nerve VIII palsy'),
        (OTHER, 'Other CN palsy'),
    ],
}

preload_data = PreloadData(
    list_data=list_data,
    model_data={},
    unique_field_data=None)
