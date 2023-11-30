# Generated by Django 4.1 on 2023-11-28 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("adventApp", "0007_character_snowballs"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ornament",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position_x", models.IntegerField(default=0)),
                ("position_y", models.IntegerField(default=0)),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adventApp.character",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gift",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position_x", models.IntegerField(default=0)),
                ("position_y", models.IntegerField(default=0)),
                ("note", models.TextField()),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_gifts",
                        to="adventApp.character",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_gifts",
                        to="adventApp.character",
                    ),
                ),
            ],
        ),
    ]