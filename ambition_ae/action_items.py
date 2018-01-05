from django.core.exceptions import ObjectDoesNotExist
from edc_action_item import Action, HIGH_PRIORITY, site_action_items
from edc_constants.constants import YES, DEAD, LOST_TO_FOLLOWUP, NO
from django.utils.safestring import mark_safe

from .email_contacts import email_contacts
from ambition_ae.constants import GRADE4, GRADE5
from ambition_prn.action_items import DEATH_REPORT_ACTION
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.models.subject_schedule_history import SubjectScheduleHistory

AE_INITIAL_ACTION = 'submit-initial-ae-report'
AE_TMG_ACTION = 'submit-ae-tmg-report'
AE_FOLLOWUP_ACTION = 'submit-ae-followup-report'
RECURRENCE_OF_SYMPTOMS_ACTION = 'submit-recurrence-of-symptoms'


class BaseNonAeInitialAction(Action):

    parent_model_fk_attr = 'ae_initial'
    show_link_to_changelist = True
    admin_site_name = 'ambition_ae_admin'
    priority = HIGH_PRIORITY

    @property
    def action_item_reason(self):
        return self.ae_initial.action_item_reason


class AeTmgAction(BaseNonAeInitialAction):
    name = AE_TMG_ACTION
    display_name = 'AE TMG Report pending'
    model = 'ambition_ae.aetmg'
    create_by_user = False
    color_style = 'info'
    show_link_to_changelist = True
    admin_site_name = 'ambition_ae_admin'
    instructions = mark_safe(
        f'This report is to be completed by the TMG only.')


class AeFollowupAction(BaseNonAeInitialAction):
    name = AE_FOLLOWUP_ACTION
    display_name = 'Submit AE Followup Report'
    model = 'ambition_ae.aefollowup'
    create_by_user = False
    show_link_to_changelist = True
    admin_site_name = 'ambition_ae_admin'
    instructions = mark_safe(
        f'Email to the TMG at <a href="mailto:'
        f'{email_contacts.get("ae_reports")}">'
        f'{email_contacts.get("ae_reports")}</a>')

    def get_next_actions(self):
        next_actions = []
        if self.model_obj.followup == YES:
            next_actions = self.append_to_next_if_required(
                next_actions=next_actions,
                action_cls=self, required=True)
        elif self.model_obj.followup == NO:
            self.delete_if_new(action_cls=self)
        # AeTmg if severity increased
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_cls=AeTmgAction,
            required=self.model_obj.ae_grade in [GRADE4, GRADE5])
        # Death report if G5/Death
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_cls=site_action_items.get(DEATH_REPORT_ACTION),
            required=self.model_obj.outcome == DEAD)
        # Study termination if LTFU
        if self.model_obj.outcome == LOST_TO_FOLLOWUP:
            # get the action class for the offschedule model
            for onschedule_model_obj in SubjectScheduleHistory.objects.onschedules(
                    subject_identifier=self.subject_identifier,
                    report_datetime=self.model_obj.report_datetime):
                _, schedule = site_visit_schedules.get_by_onschedule_model(
                    onschedule_model=onschedule_model_obj._meta.label_lower)
                offschedule_model = schedule.offschedule_model
                action_cls = site_action_items.get_by_model(
                    model=offschedule_model)
                next_actions = self.append_to_next_if_required(
                    next_actions=next_actions,
                    action_cls=action_cls)
        return next_actions


class AeInitialAction(Action):

    name = AE_INITIAL_ACTION
    display_name = 'Submit AE Initial Report'
    model = 'ambition_ae.aeinitial'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'ambition_ae_admin'
    instructions = 'Complete the initial AE report'
    priority = HIGH_PRIORITY

    def get_next_actions(self):
        """Returns next actions.
        """
        next_actions = self.append_to_next_if_required(
            action_cls=AeFollowupAction,
            required=True)
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_cls=AeTmgAction,
            required=self.model_obj.ae_grade in [GRADE4, GRADE5])
        next_actions = self.append_to_next_if_required(
            next_actions=next_actions,
            action_cls=site_action_items.get(RECURRENCE_OF_SYMPTOMS_ACTION),
            required=self.model_obj.ae_cm_recurrence == YES)
        return next_actions


class RecurrenceOfSymptomsAction(Action):
    name = RECURRENCE_OF_SYMPTOMS_ACTION
    display_name = 'Submit Recurrence of Symptoms Report'
    model = 'ambition_ae.recurrencesymptom'
    show_link_to_changelist = True
    admin_site_name = 'ambition_ae_admin'
    priority = HIGH_PRIORITY
    create_by_user = False
    help_text = 'This document is triggered by AE Initial'


site_action_items.register(AeInitialAction)
site_action_items.register(AeTmgAction)
site_action_items.register(AeFollowupAction)
site_action_items.register(RecurrenceOfSymptomsAction)
