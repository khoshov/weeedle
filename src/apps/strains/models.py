from django.db import models
from django.utils.text import slugify


class Strain(models.Model):
    TYPES = (
        (0, 'sativa'),
        (1, 'indica'),
        (2, 'hybrid'),
    )

    DIFFICULTY = (
        (0, 'easy'),
        (1, 'moderate'),
        (2, 'difficult'),
    )

    HEIGHT = (
        (0, '< 30'),
        (1, '30 - 78'),
        (2, '> 78'),
    )

    CROP = (
        (0, '0.5 - 1'),
        (1, '1 - 3'),
        (2, '3 - 6'),
    )

    FLOWERING = (
        (0, '7 - 9'),
        (1, '10 - 12'),
        (2, '> 12'),
    )
    icon = models.CharField(max_length=50, default="🌿")
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    type = models.IntegerField(choices=TYPES, blank=True, null=True)
    thc = models.CharField(max_length=255, blank=True, null=True)
    cbd = models.CharField(max_length=255, blank=True, null=True)
    difficulty = models.IntegerField(choices=DIFFICULTY, blank=True, null=True)
    height = models.IntegerField(choices=HEIGHT, blank=True, null=True)
    crop = models.IntegerField(choices=CROP, blank=True, null=True)
    flowering = models.IntegerField(choices=FLOWERING, blank=True, null=True)
    parents = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)
