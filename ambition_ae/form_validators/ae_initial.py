from edc_form_validators import FormValidator
from edc_constants.constants import YES
from ambition_rando.constants import SINGLE_DOSE, CONTROL


class AeInitialFormValidator(FormValidator):

    def clean(self):

        condition = (
            self.cleaned_data.get('regimen') == SINGLE_DOSE
            and self.cleaned_data.get(
                'ae_study_relation_possibility') == YES)
        self.applicable_if_true(
            condition=condition,
            field_applicable='ambisome_relation')

        condition = (
            self.cleaned_data.get('regimen') == CONTROL
            and self.cleaned_data.get(
                'ae_study_relation_possibility') == YES)
        self.applicable_if_true(
            condition=condition,
            field_applicable='amphotericin_b_relation')

        condition = (
            self.cleaned_data.get('regimen') == 'Control'
            or self.cleaned_data.get('regimen') == 'Single dose'
            and self.cleaned_data.get(
                'ae_study_relation_possibility') == YES)
        for drug in ['fluconazole_relation', 'flucytosine_relation']:
            self.applicable_if_true(
                condition=condition,
                field_applicable=drug)

        self.required_if(
            YES,
            field='ae_cause',
            field_required='ae_cause_other')

        self.applicable_if(
            YES,
            field='sae',
            field_applicable='sae_reason')

        self.applicable_if(
            YES,
            field='susar',
            field_applicable='susar_reported')
