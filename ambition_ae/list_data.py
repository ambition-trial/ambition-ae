from edc_list_data import PreloadData
from edc_constants.constants import OTHER, YES
from edc_action_item.models.action_type import ActionType


list_data = {
    'ambition_ae.aeclassification': [
        ('anaemia', 'Anaemia'),
        ('thrombocytopenia', 'Thrombocytopenia'),
        ('diarrhoea', 'Diarrhoea'),
        ('thrombophlebitis', 'Renal impairment'),
        ('pneumonia', 'Pneumonia'),
        ('TB', 'TB'),
        ('hypokalaemia', 'Hypokalaemia'),
        ('bacteraemia/sepsis', 'Bacteraemia/sepsis'),
        ('neutropaenia', 'Neutropaenia'),
        ('CM_IRIS', 'CM IRIS'),
        ('respiratory_distress', 'Respiratory distress'),
        (OTHER, 'Other')
    ],
}

model_data = {
    ('edc_action_item.actiontype', 'display_name'): [
        {'display_name': 'Submit initial AE report',
         'prn_form_action': YES,
         'model': 'ambition_ae.aeinitial',
         'show_on_dashboard': True,
         'instructions': 'Complete the initial report and forward to the TMG'},
        {'display_name': 'Submit AE TMG report',
         'prn_form_action': YES,
         'model': 'ambition_ae.aetmg',
         'show_on_dashboard': False,
         'instructions': None},
        {'display_name': 'Submit followup AE report',
         'prn_form_action': YES,
         'model': 'ambition_ae.aefollowup',
         'show_on_dashboard': True,
         'instructions': 'Complete the followup report and forward to the TMG'},
        {'display_name': 'Submit final AE report',
         'prn_form_action': YES,
         'model': 'ambition_ae.aefinal',
         'show_on_dashboard': True,
         'instructions': 'Complete the final report and forward to the TMG'},
    ]
}


preload_data = PreloadData(
    list_data=list_data,
    model_data=model_data,
    unique_field_data=None)

# add next action to 'Submit initial AE report'
action_type = ActionType.objects.get(display_name='Submit initial AE report')
next_action_type = ActionType.objects.get(
    display_name='Submit followup AE report')
action_type.next_action = next_action_type
action_type.save()

# add next action to 'Submit followup AE report'
action_type = ActionType.objects.get(
    display_name='Submit followup AE report')
action_type.next_action = action_type
action_type.save()
