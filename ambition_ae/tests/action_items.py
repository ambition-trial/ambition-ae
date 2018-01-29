from edc_action_item.constants import HIGH_PRIORITY
from edc_action_item.action import Action


class RecurrenceOfSymptomsAction(Action):
    name = 'submit-recurrence-of-symptoms'
    display_name = 'Submit Recurrence of Symptoms Report'
    model = 'ambition_ae.recurrencesymptom'
    show_on_dashboard = True
    priority = HIGH_PRIORITY
    create_by_user = False
    help_text = 'This document is triggered by AE Initial'
