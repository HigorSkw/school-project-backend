# Generated by Django 4.1.7 on 2023-02-26 16:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grades", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grade",
            name="note",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
    ]
