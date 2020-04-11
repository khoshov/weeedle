import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from ipinfo.utils import get_region_info
from .forms import CensorshipForm


class CensorshipFormView(FormView):
    template_name = "censorship/form.html"
    form_class = CensorshipForm
    success_url = reverse_lazy("strains:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        region_info = get_region_info(self.request)

        context['disable_search'] = True

        if region_info:
            context['country'] = region_info
            form = context['form']
            form.initial['country'] = region_info

        return context

    def form_valid(self, form):
        response = HttpResponseRedirect(self.get_success_url())
        max_age = 24 * 60 * 60
        expires = datetime.datetime.now() + datetime.timedelta(seconds=max_age)
        response.set_cookie(
            "allowed", "true", expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
        )
        return response
