# Generated by Django 4.1 on 2023-11-28 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("adventApp", "0011_labyrinth"),
    ]

    operations = [
        migrations.AddField(
            model_name="labyrinth",
            name="possessed_character",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="possessed_in_labyrinth",
                to="adventApp.character",
            ),
        ),
    ]