from django.urls import path

from . import views

app_name = "strains"

urlpatterns = [
    path("", views.StrainListView.as_view(), name="list"),
    path("<slug:slug>/", views.StrainDetailView.as_view(), name="detail"),
]
