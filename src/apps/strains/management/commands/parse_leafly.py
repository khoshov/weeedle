import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from strains.models import Strain

BASE_URL = "https://www.leafly.com/"
POPULAR_STRAINS_URL = "/strains/lists/curated/popular-marijuana-strains/"
URL = urljoin(BASE_URL, POPULAR_STRAINS_URL)


class LeaflyStrain:
    def __init__(self, strain_html):
        self.strain_html = strain_html
        self.name = self.strain_html.find("div", class_="strain-tile__name").text

    def safe_parse(self, field):
        try:
            return getattr(self, field)
        except Exception as e:
            print(f"Can't parse {field} field. {e}")

    @property
    def description(self):
        return self.strain_html.find("div", class_="strain__description").text

    @property
    def type(self):
        type_options = {"sativa": 0, "indica": 1, "hybrid": 2}
        strain_type = self.strain_html.find(
            "h2", class_="font-mono font-bold text-green text-xs"
        ).next.next
        return type_options[strain_type.lower()]

    @property
    def thc(self):
        return self.strain_html.find(
            "button", attrs={"data-testid": "cannabinoids__carrot-link-button__thc"}
        ).find_next("div", class_="font-body").next

    @property
    def difficulty(self):
        difficulty_options = {'easy': 0, 'moderate': 1, 'difficult': 2}
        difficulty = self.strain_html.find(
            "div", text=re.compile(r"^Difficulty.?")
        ).next_sibling.find("div", class_="bg-deep-green").text
        return difficulty_options[difficulty.lower()]

    @property
    def height(self):
        height_options = {'< 30': 0, '30 - 78': 1, '> 78': 2}
        height = self.strain_html.find(
            "div", text=re.compile(r"^Height.?")
        ).next_sibling.find("div", class_="bg-deep-green").text
        return height_options[height.lower()]

    @property
    def crop(self):
        crop_options = {'0.5 - 1': 0, '1 - 3': 1, '3 - 6': 2}
        crop = self.strain_html.find(
            "div", text=re.compile(r"^Yield.?")
        ).next_sibling.find("div", class_="bg-deep-green").text
        return crop_options[crop.lower()]

    @property
    def flowering(self):
        flowering_options = {'7 - 9': 0, '10 - 12': 1, '> 12': 2}
        flowering = self.strain_html.find(
            "div", text=re.compile(r"^Flowering.?")
        ).next_sibling.find("div", class_="bg-deep-green").text
        return flowering_options[flowering.lower()]

    @property
    def parents(self):
        parent_left = self.strain_html.find(
            "div", class_="lineage__left-parent"
        ).next.next.next.next.next
        parent_right = self.strain_html.find(
            "div", class_="lineage__right-parent"
        ).next.next.next.next.next
        return f'{parent_left} x {parent_right}'

    @property
    def strain_data(self):
        return {
            "name": self.name,
            "slug": slugify(self.name),
            "description": self.safe_parse("description"),
            "type": self.safe_parse("type"),
            "thc": self.safe_parse("thc"),
            "difficulty": self.safe_parse("difficulty"),
            "height": self.safe_parse("height"),
            "crop": self.safe_parse("crop"),
            "flowering": self.safe_parse("flowering"),
            "parents": self.safe_parse("parents"),
        }


class Command(BaseCommand):
    help = 'Parse leafly popular strains'

    @staticmethod
    def get_strains():
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.find_all("a", class_="strain-tile")

    @staticmethod
    def get_strain_html(strain):
        strain_page_url = strain["href"]
        r = requests.get(urljoin(BASE_URL, strain_page_url))
        return BeautifulSoup(r.text, "html.parser")

    def handle(self, *args, **options):
        strains = self.get_strains()

        for strain in strains:
            strain_html = self.get_strain_html(strain)
            strain = LeaflyStrain(strain_html)
            strain_exists = Strain.objects.filter(name=strain.name).exists()
            if strain_exists:
                continue
            Strain.objects.create(**strain.strain_data)
