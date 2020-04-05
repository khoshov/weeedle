import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import CensorshipForm


class CensorshipFormView(FormView):
    template_name = "censorship/form.html"
    form_class = CensorshipForm
    success_url = reverse_lazy("strains:list")

    def form_valid(self, form):
        response = HttpResponseRedirect(self.get_success_url())
        max_age = 24 * 60 * 60
        expires = datetime.datetime.now() + datetime.timedelta(seconds=max_age)
        response.set_cookie(
            "allowed", "true", expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disable_search'] = True
        return context
