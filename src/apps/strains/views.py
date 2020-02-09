from django.db.models import Min, Max
from django.views.generic import DetailView
from django_filters.views import FilterView
from el_pagination.views import AjaxListView

from strains.constants import STRAIN_FILTER_DATA
from strains.filters import StrainFilter
from strains.models import Strain


class StrainListView(FilterView, AjaxListView):
    context_object_name = "strains"
    template_name = "strains/strain_list.html"
    page_template = "strains/strain_list_page.html"
    filterset_class = StrainFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filters"] = STRAIN_FILTER_DATA
        context["thc"] = Strain.objects.all().aggregate(Min("thc"), Max("thc"))
        return context


class StrainDetailView(DetailView):
    model = Strain
    context_object_name = "strain"
    template_name = "strains/strain_detail.html"
    slug_url_kwarg = "slug"
    slug_field = "slug"
