from .utils import get_region_info


class IPInfoMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if request.COOKIES.get('geoip_region') is not None:
            region = request.COOKIES.get('geoip_region', None)
        else:
            region = get_region_info(request)

        if region:
            # Для тестирования региона
            overwrite_region = request.COOKIES.get('geoip_region')
            if overwrite_region:
                region = overwrite_region

        request.META['region'] = region if region else None

        response = self.get_response(request)
        return response
