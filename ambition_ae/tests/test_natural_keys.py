from ambition_rando.tests import AmbitionTestCaseMixin
from django.apps import apps as django_apps
from django.test import TestCase, tag
from django.test.utils import override_settings
from edc_base.model_mixins import ListModelMixin
from edc_metadata.tests import CrfTestHelper
from edc_registration.models import RegisteredSubject
from edc_sync.tests import SyncTestHelper
from model_mommy import mommy
from edc_sync.models import OutgoingTransaction
from pprint import pprint


@tag('sync')
@override_settings(SITE_ID='10')
class TestNaturalKey(AmbitionTestCaseMixin, TestCase):

    sync_test_helper = SyncTestHelper()
    crf_test_helper = CrfTestHelper()

    def setUp(self):
        self.subject_identifier = '12345'
        RegisteredSubject.objects.create(
            subject_identifier=self.subject_identifier)

    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr('ambition_ae')

    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr(
            'ambition_ae')

    def complete_non_crf_models(self, exclude_models=None):
        exclude_models = exclude_models or []
        completed_models = []
        models = django_apps.get_app_config('ambition_ae').get_models()
        for model in models:
            if ((model._meta.label_lower not in exclude_models and
                    not issubclass(model, ListModelMixin)) and
                    not model._meta.label_lower.startswith('ambition_ae.historical')):
                completed_models.append(
                    mommy.make_recipe(
                        model._meta.label_lower,
                        subject_identifier=self.subject_identifier))
        return completed_models

    def test_deserialize_ae_initial(self):
        ae_initial = mommy.make_recipe(
            'ambition_ae.aeinitial',
            subject_identifier=self.subject_identifier)
        pprint(ae_initial.__dict__)
        for outgoing_transaction in OutgoingTransaction.objects.filter(
                tx_name=ae_initial._meta.label_lower):
            self.sync_test_helper.sync_test_deserialize(
                ae_initial, outgoing_transaction)

    def test_deserialize_ae_tmg(self):
        ae_initial = mommy.make_recipe(
            'ambition_ae.aeinitial',
            subject_identifier=self.subject_identifier)
        ae_tmg = mommy.make_recipe(
            'ambition_ae.aetmg',
            ae_initial=ae_initial,
            subject_identifier=self.subject_identifier)
        for outgoing_transaction in OutgoingTransaction.objects.filter(
                tx_name=ae_tmg._meta.label_lower):
            self.sync_test_helper.sync_test_deserialize(
                ae_tmg, outgoing_transaction)

    def test_deserialize_recurrence_symptom(self):
        recurrence_symptoms = mommy.make_recipe(
            'ambition_ae.recurrencesymptom',
            subject_identifier=self.subject_identifier)
        for outgoing_transaction in OutgoingTransaction.objects.filter(
                tx_name=recurrence_symptoms._meta.label_lower):
            self.sync_test_helper.sync_test_deserialize(
                recurrence_symptoms, outgoing_transaction)
