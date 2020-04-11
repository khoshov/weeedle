from .utils import get_request_info
from .conf import settings


class IPInfoMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        ipinfo = get_request_info(request)
        if ipinfo is not None:
            # Для тестирования региона
            overwrite_region = request.COOKIES.get('region')
            if overwrite_region:
                ipinfo.region = overwrite_region

            request.META[settings.IPINFO_META_KEY] = ipinfo
        response = self.get_response(request)
        return response
