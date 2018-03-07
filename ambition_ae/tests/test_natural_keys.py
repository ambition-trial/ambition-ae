from django.test import TestCase, tag
from django.test.utils import override_settings
from edc_metadata.tests import CrfTestHelper
from edc_sync.tests import SyncTestHelper


@override_settings(SITE_ID='10')
class TestNaturalKey(TestCase):

    sync_test_helper = SyncTestHelper()
    crf_test_helper = CrfTestHelper()

    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr('ambition_ae')

    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr(
            'ambition_ae')
