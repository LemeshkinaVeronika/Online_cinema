# Generated by Django 5.0.6 on 2024-06-20 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieblog', '0018_ratemodel_delete_rate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratemodel',
            options={'verbose_name': 'Оценки', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.RenameField(
            model_name='ratemodel',
            old_name='rate',
            new_name='rate_number',
        ),
    ]
