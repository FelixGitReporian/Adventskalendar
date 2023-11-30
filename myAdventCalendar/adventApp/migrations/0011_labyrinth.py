# Generated by Django 4.1 on 2023-11-28 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("adventApp", "0010_remove_character_hits_received_snowballhit"),
    ]

    operations = [
        migrations.CreateModel(
            name="Labyrinth",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("start_time", models.DateTimeField(blank=True, null=True)),
                ("background_image", models.ImageField(upload_to="decisions/")),
                (
                    "next_decision_a",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="adventApp.labyrinth",
                    ),
                ),
                (
                    "next_decision_b",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="adventApp.labyrinth",
                    ),
                ),
            ],
        ),
    ]
