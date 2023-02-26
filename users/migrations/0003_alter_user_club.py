# Generated by Django 4.1.7 on 2023-02-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clubs", "0002_initial"),
        ("users", "0002_remove_user_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="club",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clubs",
                to="clubs.club",
            ),
        ),
    ]
