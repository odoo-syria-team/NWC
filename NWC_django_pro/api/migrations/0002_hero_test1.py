# Generated by Django 5.0.1 on 2024-02-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='test1',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='عنوان '),
        ),
    ]
