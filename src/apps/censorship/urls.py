from django.urls import path

from . import views

app_name = "censorship"

urlpatterns = [
    path("", views.CensorshipFormView.as_view(), name="form"),
]
