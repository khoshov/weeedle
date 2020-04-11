from django.conf import settings
from appconf import AppConf


class IpInfoAppConf(AppConf):
    META_KEY = 'IP_INFO'
    CACHE_TIMEOUT = 0
    DB_TIMEOUT = 0
    IPSTACK_KEY = '7284aca457c2371982917eaceb341ed7'
