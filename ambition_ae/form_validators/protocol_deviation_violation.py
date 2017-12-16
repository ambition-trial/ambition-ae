from django.forms import forms
from edc_form_validators import FormValidator, NOT_REQUIRED_ERROR
from edc_constants.constants import YES, OTHER

from ..constants import DEVIATION


class ProtocolDeviationViolationFormValidator(FormValidator):

    def clean(self):

        self.validate_other_specify(
            field='protocol_violation_type',
            other_specify_field='protocol_violation_type_other',
            other_stored_value=OTHER)

        field_required_list = [
            'date_violation_datetime',
            'protocol_violation_type',
            'violation_description',
            'violation_reason']
        for field_required in field_required_list:
            self.not_required_if(
                DEVIATION,
                field='deviation_or_violation',
                field_required=field_required)

        self.required_if(
            YES,
            field='participant_safety_impact',
            field_required='participant_safety_impact_details')

        self.required_if(
            YES,
            field='study_outcomes_impact',
            field_required='study_outcomes_impact_details')

        self.require_together(
            field='corrective_action_datetime',
            field_required='corrective_action')

        self.require_together(
            field='preventative_action_datetime',
            field_required='preventative_action')
