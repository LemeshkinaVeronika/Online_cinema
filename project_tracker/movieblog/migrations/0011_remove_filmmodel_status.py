# Generated by Django 4.2.13 on 2024-06-11 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieblog', '0010_alter_filmmodel_director_alter_filmmodel_full_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmmodel',
            name='status',
        ),
    ]