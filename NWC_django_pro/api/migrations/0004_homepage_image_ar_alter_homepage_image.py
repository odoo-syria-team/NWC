# Generated by Django 5.0.1 on 2024-02-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_hero_test_remove_hero_test1'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image_ar',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة في مقطع حولنا'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='image in about us section '),
        ),
    ]