# Generated by Django 5.0.6 on 2024-06-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieblog', '0019_alter_ratemodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmmodel',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ratemodel',
            name='rate_number',
            field=models.FloatField(default=0),
        ),
    ]
