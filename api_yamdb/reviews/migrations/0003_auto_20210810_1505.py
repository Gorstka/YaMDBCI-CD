# Generated by Django 2.2.16 on 2021-08-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_titles_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="titles",
            name="description",
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
