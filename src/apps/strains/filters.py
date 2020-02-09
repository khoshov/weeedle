import django_filters

from .models import Strain


class StrainFilter(django_filters.FilterSet):
    type = django_filters.MultipleChoiceFilter(choices=Strain.TYPES)
    difficulty = django_filters.MultipleChoiceFilter(choices=Strain.DIFFICULTY)
    height = django_filters.MultipleChoiceFilter(choices=Strain.HEIGHT)
    crop = django_filters.MultipleChoiceFilter(choices=Strain.CROP)
    flowering = django_filters.MultipleChoiceFilter(choices=Strain.FLOWERING)

    class Meta:
        model = Strain
        fields = ['type', 'thc', 'difficulty', 'height', 'crop', 'flowering', ]
