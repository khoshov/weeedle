# Generated by Django 2.2.6 on 2020-02-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("strains", "0002_strain_short"),
    ]

    operations = [
        migrations.AddField(
            model_name="strain",
            name="icon",
            field=models.CharField(default="", max_length=50),
        ),
    ]
