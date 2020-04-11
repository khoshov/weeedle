from django.db import models
from django.utils.translation import ugettext_lazy as _
from .conf import IpInfoAppConf


class IpInfo(models.Model):
    ip = models.GenericIPAddressField(_('ip'), unique=True)
    city = models.CharField(_('city'), max_length=255)
    region = models.CharField(_('region'), max_length=255)
    country = models.CharField(_('country'), max_length=255)
    latitude = models.DecimalField(_('latitude'), max_digits=8, decimal_places=4)
    longitude = models.DecimalField(_('longitude'), max_digits=8, decimal_places=4)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('IpInfo')
        verbose_name_plural = _('IpInfo')
        unique_together = ('ip', 'updated')
