# Generated by Django 5.0.6 on 2024-06-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movieblog", "0017_userfilmlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfilmlist",
            name="list_type",
            field=models.CharField(
                choices=[
                    ("izbrannoe", "Избранное"),
                    ("posmotreno", "Просмотренное"),
                    ("budu-smotret", "Буду смотреть"),
                ],
                max_length=20,
            ),
        ),
    ]
