from django.test import TestCase, RequestFactory
from .conf import settings
from . import providers, utils

IP_TESTS = {
    '66.249.69.61': {
        'city': 'Mountain View',
        'region': 'California',
    },
    '162.246.155.16': {
        'ip': '162.246.155.16',
        'city': 'Hartwell',
        'country': 'US',
        'region': 'Georgia',
    },
    '90.155.128.74': {
        'city': ['Moscow', 'Odintsovo'],
        'region': ['Moscow', 'Moscow Oblast'],
    },
    '2600:3c00::f03c:91ff:fe67:aa7c': {
        'city': 'Dallas',
        'region': 'Texas',
    },
    '2a02:6b8:0:811:24d0:61b6:a089:21c4': {
        'city': 'Moscow',
        'region': 'Moscow',
    },
}


class TestProviders(TestCase):
    def _checkInfo(self, value, standard):
        for key, standard_value in standard.items():
            if isinstance(standard_value, (list, tuple)):
                self.assertIn(value[key], standard_value)
            else:
                self.assertEqual(value[key], standard_value)

    def test_ipapi(self):
        for ip, check_data in IP_TESTS.items():
            info = providers.ipapi(ip)
            self._checkInfo(info, check_data)

    def test_freegeoip(self):
        for ip, check_data in IP_TESTS.items():
            info = providers.freegeoip(ip)
            self._checkInfo(info, check_data)

    def test_ipinfo(self):
        for ip, check_data in IP_TESTS.items():
            info = providers.ipinfo(ip)
            self._checkInfo(info, check_data)


class TestUtils(TestCase):
    def test_get_info(self):
        for ip, check_data in IP_TESTS.items():
            utils.CacheStorage.delete(ip)

            ipinfo = utils.get_info(ip)

            cache_info = utils.CacheStorage.load(ip)
            self.assertEqual(ipinfo, cache_info)

            db_info = utils.DBStorage.load(ip)
            self.assertEqual(ipinfo, db_info)

    def test_request_empty(self):
        rf = RequestFactory()
        request = rf.get('/')
        self.assertIsNone(utils.get_request_info(request))

    def test_request_ip(self):
        rf = RequestFactory()
        request = rf.get('/')
        ipinfo = utils.get_info('66.249.69.61')
        request.META['REMOTE_ADDR'] = '66.249.69.61'
        self.assertEqual(ipinfo, utils.get_request_info(request))

    def test_request_meta(self):
        rf = RequestFactory()
        request = rf.get('/')
        ipinfo = utils.get_info('66.249.69.61')
        request.META[settings.IPINFO_META_KEY] = ipinfo
        self.assertEqual(ipinfo, utils.get_request_info(request))
