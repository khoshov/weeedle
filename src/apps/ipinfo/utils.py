import os

from django.conf import settings
from geoip2.database import Reader
from geoip2.errors import AddressNotFoundError
from ipware.ip import get_real_ip
from ipware.utils import is_valid_ip


def get_region_info(request):
    if not request:
        return None
    ip = get_real_ip(request)

    region = None

    if ip is not None and isinstance(ip, str) and is_valid_ip(ip):
        db_path = os.path.join(settings.BASE_DIR, 'apps/ipinfo/GeoLite2-City.mmdb')
        reader = Reader(db_path)

        try:
            response = reader.city(ip)

            region = response.subdivisions[0].name

            return region
        except (AddressNotFoundError, IndexError):
            pass

    return region
