# Generated by Django 5.0.6 on 2024-07-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movieblog", "0021_userfilmlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="filmmodel",
            name="link_to_player",
            field=models.CharField(
                default="", max_length=200, verbose_name="Ссылка на плеер"
            ),
        ),
    ]
