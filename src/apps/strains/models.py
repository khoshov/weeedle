from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Strain(models.Model):
    TYPES = (
        (0, _("Сатива")),
        (1, _("Индика")),
        (2, _("Гибрид")),
    )

    DIFFICULTY = (
        (0, _("Легкая")),
        (1, _("Средняя")),
        (2, _("Высокая")),
    )

    HEIGHT = (
        (0, "< 30"),
        (1, "30 - 78"),
        (2, "> 78"),
    )

    CROP = (
        (0, "0.5 - 1"),
        (1, "1 - 3"),
        (2, "3 - 6"),
    )

    FLOWERING = (
        (0, "7 - 9"),
        (1, "10 - 12"),
        (2, "> 12"),
    )
    icon = models.CharField(max_length=50, verbose_name=_("Иконка"), default="🌿")
    name = models.CharField(max_length=255, verbose_name=_("Название сорта"))
    slug = models.SlugField(verbose_name=_("Slug"))
    description = models.TextField(blank=True, verbose_name=_("Описание"), null=True)
    type = models.IntegerField(
        choices=TYPES, verbose_name=_("Тип"), blank=True, null=True
    )
    thc = models.CharField(max_length=255, verbose_name=_("ТГК"), blank=True, null=True)
    cbd = models.CharField(max_length=255, verbose_name=_("КБД"), blank=True, null=True)
    difficulty = models.IntegerField(
        choices=DIFFICULTY,
        verbose_name=_("Сложность выращивания"),
        blank=True,
        null=True,
    )
    height = models.IntegerField(
        choices=HEIGHT, verbose_name=_("Высота растения"), blank=True, null=True
    )
    crop = models.IntegerField(
        choices=CROP, verbose_name=_("Урожайность"), blank=True, null=True
    )
    flowering = models.IntegerField(
        choices=FLOWERING, verbose_name=_("Время цветения"), blank=True, null=True
    )
    parents = models.CharField(
        max_length=255, verbose_name=_("Генетика"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Сорт")
        verbose_name_plural = _("Сорта")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)
