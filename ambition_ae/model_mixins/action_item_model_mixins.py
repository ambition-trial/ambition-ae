from django.core.exceptions import ObjectDoesNotExist
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_action_item.models import ActionItem
from edc_constants.constants import YES

from ..action_items import AE_INITIAL_ACTION, AE_TMG_ACTION, RECURRENCE_OF_SYMPTOMS_ACTION


class AeInitialActionItemModelMixin(ActionItemModelMixin):

    def creates_action_items(self):
        action_items = [AE_INITIAL_ACTION]
        return action_items

    def create_next_action_items(self, action_type_name=None):
        action_items = []
        if action_type_name:
            action_items.append(action_type_name)
        try:
            ActionItem.objects.get(
                subject_identifier=self.subject_identifier,
                parent_reference_identifier=self.tracking_identifier,
                reference_model='ambition_ae.aetmg')
        except ObjectDoesNotExist:
            action_items.append(AE_TMG_ACTION)
        if self.ae_cm_recurrence == YES:
            action_items.append(RECURRENCE_OF_SYMPTOMS_ACTION)
        return action_items

    class Meta:
        abstract = True


class AeFollowupActionItemModelMixin(ActionItemModelMixin):

    def create_next_action_items(self, action_type_name=None):
        action_items = []
        if self.followup == YES:
            action_items.append(action_type_name)
        else:
            action_items.append('submit-final-ae-report')
        return action_items

    class Meta:
        abstract = True
