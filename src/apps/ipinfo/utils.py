from ipware.utils import is_valid_ip, is_valid_ipv4
from django.core.cache import caches
from django.utils.timezone import now, timedelta
from .models import IpInfo
from .conf import settings
from . import providers

NO_IPINFO = 'empty'
cache = caches['default']


def _request(ip):
    """
    Получение информации от одного из сервисов.

    :param ip: str
    :return: dict | None
    """
    ipinfo = providers.ipinfo(ip)
    if ipinfo is not None and ipinfo['region']:
        return ipinfo

    ipinfo = providers.freegeoip(ip)
    if ipinfo is not None and ipinfo['region']:
        return ipinfo

    ipinfo = providers.ipapi(ip)
    if ipinfo is not None and ipinfo['region']:
        return ipinfo

    return None


class CacheStorage:
    @staticmethod
    def _make_key(ip):
        return 'ip:{}'.format(ip)

    @classmethod
    def load(cls, ip):
        cache_key = cls._make_key(ip)
        if cache_key in cache:
            return cache.get(cache_key)

    @classmethod
    def save(cls, ip, value):
        cache_key = cls._make_key(ip)
        cache.set(cache_key, value, settings.IPINFO_CACHE_TIMEOUT)
        return value

    @classmethod
    def delete(cls, ip):
        cache_key = cls._make_key(ip)
        if cache_key in cache:
            return cache.delete(cache_key)


class DBStorage:
    @staticmethod
    def load(ip):
        try:
            ipinfo = IpInfo.objects.get(ip=ip)
        except IpInfo.DoesNotExist:
            return
        else:
            min_time = now() - timedelta(seconds=settings.IPINFO_DB_TIMEOUT)
            if ipinfo.updated > min_time:
                return ipinfo

    @staticmethod
    def save(ip, info):
        ipinfo, created = IpInfo.objects.update_or_create(
            ip=ip,
            defaults={
                'city': info['city'] or '',
                'region': info['region'] or '',
                'country': info['country'] or '',
                'latitude': info['latitude'],
                'longitude': info['longitude'],
            }
        )
        return ipinfo


def get_info(ip):
    """
    Получение информации по IP.

    :param ip: str
    :return: IpInfo | None
    """
    ipinfo = CacheStorage.load(ip)
    
    if ipinfo == NO_IPINFO:
        return None
    elif ipinfo is not None:
        return ipinfo

    ipinfo = DBStorage.load(ip)
    if ipinfo is not None:
        CacheStorage.save(ip, ipinfo)
        return ipinfo
    info = _request(ip)
    if info is None:
        # Сохранение информации об отстуствии данных
        CacheStorage.save(ip, NO_IPINFO)
    else:
        ipinfo = DBStorage.save(ip, info)
        CacheStorage.save(ip, ipinfo)
        return ipinfo

    return None


def get_request_info(request):
    """
    Получение информации из объекта request.

    :param request: django.core.handlers.wsgi.WSGIRequest
    :return: IpInfo | None
    """
    if not request:
        return None
    ipinfo = request.META.get(settings.IPINFO_META_KEY)
    if ipinfo is not None:
        return ipinfo

    ip1 = request.META.get('HTTP_CF_CONNECTING_IP')
    ip2 = request.META.get('REMOTE_ADDR')

    if isinstance(ip1, str) and is_valid_ipv4(ip1):
        ipinfo = get_info(ip1)
        if ipinfo is not None:
            return ipinfo
    elif isinstance(ip2, str) and is_valid_ipv4(ip2):
        ipinfo = get_info(ip2)
        if ipinfo is not None:
            return ipinfo
    else:
        return None
