# Generated by Django 2.2.6 on 2020-02-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("strains", "0004_remove_strain_short"),
    ]

    operations = [
        migrations.AlterField(
            model_name="strain",
            name="icon",
            field=models.CharField(default="🌿", max_length=50),
        ),
    ]