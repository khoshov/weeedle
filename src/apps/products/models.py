from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductOptionType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Тип опции"))

    class Meta:
        verbose_name = _("Тип опции продукта")
        verbose_name_plural = _("Типы опций продукта")

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    name = models.ForeignKey(
        ProductOptionType, on_delete=models.CASCADE, verbose_name=_("Опция")
    )
    value = models.CharField(max_length=255, verbose_name=_("Значение"))

    class Meta:
        verbose_name = _("Опция продукта")
        verbose_name_plural = _("Опции продукта")

    def __str__(self):
        return f"{self.name}: {self.value}"


class Delivery(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Имя"))

    class Meta:
        verbose_name = _("Варианты доставки")
        verbose_name_plural = _("Варианты доставки")

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Имя"))

    class Meta:
        verbose_name = _("Варианты оплаты")
        verbose_name_plural = _("Варианты оплаты")

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Имя"))
    delivery_options = models.ManyToManyField(
        Delivery, verbose_name=_("Варианты доставки"), blank=True
    )
    payment_options = models.ManyToManyField(
        Payment, verbose_name=_("Варианты оплаты"), blank=True
    )

    class Meta:
        verbose_name = _("Магазин")
        verbose_name_plural = _("Магазины")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название товара"))
    producer = models.CharField(max_length=255, verbose_name=_("Производитель"))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Цена"))
    package = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Упаковка")
    )
    shop = models.ManyToManyField(Shop, verbose_name=_("Магазин"), blank=True,)
    url = models.URLField(verbose_name=_("Ссылка на страницу магазина"))
    product_options = models.ManyToManyField(
        ProductOption, verbose_name=_("Опции товара"), blank=True
    )

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")

    def __str__(self):
        return self.name
