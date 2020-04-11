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
        reader = Reader('apps/ipinfo/GeoLite2-City.mmdb')

        try:
            response = reader.city(ip)

            region = response.subdivisions[0].name

            return region
        except (AddressNotFoundError, IndexError) as e:
            pass

    return region
