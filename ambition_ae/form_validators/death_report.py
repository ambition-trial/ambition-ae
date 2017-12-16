import pytz

from django.conf import settings
from django.forms import forms
from edc_form_validators import FormValidator, NOT_REQUIRED_ERROR
from edc_constants.constants import OTHER
from edc_registration.models import RegisteredSubject

from ..constants import TUBERCULOSIS
from edc_base.utils import convert_php_dateformat
from django.utils.timezone import localtime
from django.utils.formats import localize
from arrow.arrow import Arrow


class DeathReportFormValidator(FormValidator):

    def clean(self):

        self.validate_study_day()

        self.validate_other_specify(
            field='cause_of_death',
            other_specify_field='cause_of_death_other',
            other_stored_value=OTHER)

        self.required_if(
            TUBERCULOSIS,
            field='cause_of_death',
            field_required='tb_site')

    def validate_study_day(self):
        # note: study-day is 1-based
        study_day = self.cleaned_data.get('study_day')
        if study_day:
            death_datetime = self.cleaned_data.get('death_datetime')
            if death_datetime:
                randomization_datetime = RegisteredSubject.objects.get(
                    subject_identifier=self.cleaned_data.get(
                        'subject_identifier')).randomization_datetime
                days_on_study = (
                    death_datetime.date() - randomization_datetime.date()).days
                if study_day - 1 != days_on_study:
                    tz = pytz.timezone(settings.TIME_ZONE)
                    formatted_date = Arrow.fromdatetime(
                        randomization_datetime).to(tz).strftime(
                            convert_php_dateformat(settings.DATETIME_FORMAT))
                    message = {
                        'study_day': (f'Expected study day "{days_on_study + 1}". '
                                      f'Subject was randomization on {formatted_date}')}
                    raise forms.ValidationError(
                        message, code=NOT_REQUIRED_ERROR)
