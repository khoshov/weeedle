from django.contrib import admin

from .models import Delivery, Payment, Product, ProductOption, ProductOptionType, Shop


@admin.register(ProductOptionType)
class ProductOptionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Delivery)
class ProductDeliveryAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class ProductPaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
