from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class CensorshipForm(forms.Form):
    country = CountryField(verbose_name=_("Выберите вашу страну")).formfield()
    adult = forms.BooleanField(
        label=_("Мне уже есть 18"),
        help_text=_(
            "Этот сайт содержит информацию не предназначенную для просмотра лицам младше 18 лет"
        ),
        required=False,
    )
    helper = FormHelper()
    helper.add_input(Submit("submit", "Перейти на сайт", css_class="btn-primary"))
    helper.form_method = "POST"

    def clean(self):
        cleaned_data = super().clean()
        country = cleaned_data.get("country")
        adult = cleaned_data.get("adult")

        if country == "RU":
            self.add_error("country", "Для вашего региона доступ на сайт ограничен")

        if not adult:
            self.add_error(
                "adult",
                "Этот сайт содержит информацию не предназначенную для просмотра лицам младше 18 лет.",
            )
