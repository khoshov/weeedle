from django.http import HttpResponseRedirect
from django.urls import reverse


class CensorshipMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        redirect_url = reverse("censorship:form")
        if not request.COOKIES.get("allowed") and request.path != redirect_url:
            return HttpResponseRedirect(redirect_url)
        response = self.get_response(request)
        return response
