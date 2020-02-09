from django.contrib import admin

from .models import Strain


@admin.register(Strain)
class StrainAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
