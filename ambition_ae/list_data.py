from edc_list_data import PreloadData
from edc_constants.constants import OTHER
# from edc_action_item.models.action_type import ActionType


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

preload_data = PreloadData(
    list_data=list_data,
    model_data={},
    unique_field_data=None)

# # add next action to 'Submit initial AE report'
# action_type = ActionType.objects.get(display_name='Submit initial AE report')
# next_action_type = ActionType.objects.get(
#     display_name='Submit followup AE report')
# action_type.next_action = next_action_type
# action_type.save()
#
# # add next action to 'Submit followup AE report'
# action_type = ActionType.objects.get(
#     display_name='Submit followup AE report')
# action_type.next_action = action_type
# action_type.save()
