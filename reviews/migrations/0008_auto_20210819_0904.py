# Generated by Django 2.2.6 on 2021-08-19 06:04

import django.db.models.deletion
from django.db import migrations, models

import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0007_auto_20210818_1822"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Categories",
            new_name="Category",
        ),
        migrations.RenameModel(
            old_name="Genres",
            new_name="Genre",
        ),
        migrations.AlterField(
            model_name="title",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="titles",
                to="reviews.Category",
            ),
        ),
        migrations.AlterField(
            model_name="title",
            name="year",
            field=models.PositiveSmallIntegerField(
                validators=[reviews.models.Title.year_validator]
            ),
        ),
    ]
