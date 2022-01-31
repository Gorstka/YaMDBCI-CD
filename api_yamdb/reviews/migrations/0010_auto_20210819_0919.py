# Generated by Django 2.2.6 on 2021-08-19 06:19

import reviews.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0009_auto_20210819_0914"),
    ]

    operations = [
        migrations.AlterField(
            model_name="title",
            name="year",
            field=models.PositiveSmallIntegerField(
                validators=[reviews.models.Title.year_validator]
            ),
        ),
    ]
