# Generated by Django 4.1 on 2023-11-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adventApp", "0003_character_is_taken"),
    ]

    operations = [
        migrations.AddField(
            model_name="adventnumber",
            name="color",
            field=models.CharField(default="#FFFFFF", max_length=7),
        ),
        migrations.AddField(
            model_name="adventnumber",
            name="rotation",
            field=models.IntegerField(default=0),
        ),
    ]
