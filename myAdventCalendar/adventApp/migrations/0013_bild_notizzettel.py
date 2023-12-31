# Generated by Django 4.1 on 2023-11-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adventApp", "0012_labyrinth_possessed_character"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bild",
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
                ("titel", models.CharField(max_length=100)),
                ("bild", models.ImageField(upload_to="bilder/")),
                ("hochladedatum", models.DateTimeField(auto_now_add=True)),
                ("x_position", models.IntegerField(default=0)),
                ("y_position", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Notizzettel",
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
                ("titel", models.CharField(max_length=100)),
                ("inhalt", models.TextField()),
                ("erstellungsdatum", models.DateTimeField(auto_now_add=True)),
                ("x_position", models.IntegerField(default=0)),
                ("y_position", models.IntegerField(default=0)),
            ],
        ),
    ]
