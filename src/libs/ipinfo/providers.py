import json
from decimal import Decimal
from urllib.request import urlopen
from .conf import settings


def ipapi(ip, timeout=2):
    """
    Запрос к http://ip-api.com/
    Ограничение: 150 в минуту.
    IPv6: да.

    :rtype: dict
    """
    try:
        urlresult = urlopen('http://ip-api.com/json/{}'.format(ip), timeout=timeout)
        response = urlresult.read()
        geo = json.loads(response.decode())
        if geo.get('status') != 'success':
            return None

        return {
            'ip': geo.get('query', ''),
            'city': geo.get('city', ''),
            'region': geo.get('regionName', ''),
            'country': geo.get('countryCode', ''),
            'latitude': Decimal(str(geo.get('lat', 0))),
            'longitude': Decimal(str(geo.get('lon', 0))),
        }
    except Exception:
        return None


def freegeoip(ip, timeout=2):
    """
    Запрос к http://ipstack.com/
    Ограничение: 10000 в месяц.
    IPv6: да.

    :rtype: dict
    """
    try:
        urlresult = urlopen('http://api.ipstack.com/{}?access_key={}'.format(ip, settings.IPINFO_IPSTACK_KEY), timeout=timeout)
        response = urlresult.read()
        geo = json.loads(response.decode())
        if not geo.get('country_code'):
            return None

        return {
            'ip': geo.get('ip', ''),
            'city': geo.get('city', ''),
            'region': geo.get('region_name', ''),
            'country': geo.get('country_code', ''),
            'latitude': Decimal(str(geo.get('latitude', 0))),
            'longitude': Decimal(str(geo.get('longitude', 0))),
        }
    except Exception:
        return None


def ipinfo(ip, timeout=2):
    """
    Запрос к https://ipinfo.io/
    Ограничение: 1000 в день.
    IPv6: да.

    :rtype: dict
    """
    try:
        urlresult = urlopen('https://ipinfo.io/{}/json'.format(ip), timeout=timeout)
        response = urlresult.read()
        geo = json.loads(response.decode())
        if geo.get('error'):
            return None

        lat, lng = 0, 0
        coords = geo.get('loc')
        if coords:
            lat, lng = coords.split(',')

        return {
            'ip': geo.get('ip', ''),
            'city': geo.get('city', ''),
            'region': geo.get('region', ''),
            'country': geo.get('country', ''),
            'latitude': Decimal(lat),
            'longitude': Decimal(lng),
        }
    except Exception:
        return None
