# Generated by Django 5.0.1 on 2024-02-06 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_hero_test1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='test',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='test1',
        ),
    ]