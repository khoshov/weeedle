import django_filters

from .models import Strain


class StrainFilter(django_filters.FilterSet):
    type = django_filters.MultipleChoiceFilter(choices=Strain.TYPES)
    difficulty = django_filters.MultipleChoiceFilter(choices=Strain.DIFFICULTY)
    height = django_filters.MultipleChoiceFilter(choices=Strain.HEIGHT)
    crop = django_filters.MultipleChoiceFilter(choices=Strain.CROP)
    flowering = django_filters.MultipleChoiceFilter(choices=Strain.FLOWERING)
    search = django_filters.CharFilter(field_name="name", method="search_filter")

    class Meta:
        model = Strain
        fields = ['type', 'thc', 'difficulty', 'height', 'crop', 'flowering', 'search']

    # noinspection PyMethodMayBeStatic
    def search_filter(self, queryset, name, value):
        lookup = '__'.join([name, 'icontains'])
        return queryset.filter(**{lookup: value})
