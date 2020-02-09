from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StrainsConfig(AppConfig):
    name = "strains"
    verbose_name = _("Сорта")
