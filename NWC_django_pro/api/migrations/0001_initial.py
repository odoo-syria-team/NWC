# Generated by Django 5.0.1 on 2024-02-06 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='تظهر في الموقع ؟ / Show in webSite ? ')),
                ('aboutus_en', models.TextField(max_length=2000, verbose_name='About US ')),
                ('aboutus_ar', models.TextField(blank=True, default='', max_length=2000, verbose_name='حولنا ')),
                ('title_hero_en', models.TextField(blank=True, default='', max_length=2000, verbose_name='Title')),
                ('title_hero_ar', models.TextField(blank=True, default='', max_length=2000, verbose_name='العنوان')),
                ('subtitle_hero_en', models.TextField(blank=True, default='', max_length=2000, verbose_name='Subtitle ')),
                ('subtitle_hero_ar', models.TextField(blank=True, default='', max_length=2000, verbose_name='العنوان الفرعي ')),
                ('text_hero_en', models.TextField(blank=True, default='', max_length=2000, verbose_name='Text ')),
                ('text_hero_ar', models.TextField(blank=True, default='', max_length=2000, verbose_name='النص ')),
                ('image_hero', models.ImageField(blank=True, upload_to='images/', verbose_name='Image in section about us ')),
                ('image_hero_ar', models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة في مقطع حولنا')),
                ('title_parent_en', models.CharField(blank=True, max_length=2000, verbose_name='Title in section our parent company ')),
                ('title_parent_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان في مقطع شركتنا الأم ')),
                ('subTitle_parent_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Subtitle section our parent company ')),
                ('subTitle_parent_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان الفرعي غي مقطع شركتنا الأم ')),
                ('text_parent_en', models.TextField(blank=True, default='', max_length=2000, verbose_name='Text in section our parent company ')),
                ('text_parent_ar', models.TextField(blank=True, default='', max_length=2000, verbose_name='النص في مقطع شركتنا الأم')),
                ('image_parent', models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة في مقطع شركتنا الأم / Image in section our parent company ')),
                ('logo_parent', models.ImageField(blank=True, upload_to='images/', verbose_name='الشعار في مقطع شركتنا الأم / Logo in section our parent company ')),
                ('title_our_partner_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Titel in Secion Our Partners ')),
                ('title_our_partner_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان في مقطع جميع العملاء ')),
                ('sub_title_our_partner_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Sub Titel in Secion Our Partners ')),
                ('sub_title_our_partner_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان الفرعي في مقطع جميع العملاء ')),
                ('title_our_vision_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Titel in Secion Our Vision ')),
                ('title_our_vision_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان في مقطع رؤيتنا')),
                ('text_our_vision_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Text in Secion Our Vision ')),
                ('text_our_vision_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='النص في مقطع رؤيتنا')),
                ('image_our_vision', models.ImageField(blank=True, upload_to='images/', verbose_name='Image in section our vision ')),
                ('image_our_vision_ar', models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة في مقطع رؤيتنا ')),
                ('title_our_values_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Titel in Secion Our Values ')),
                ('title_our_values_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان في مقطع مبادئنا')),
            ],
            options={
                'verbose_name': 'About U',
            },
        ),
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='تظهر في الموقع ؟ / Show in webSite ?  ')),
                ('company_name_en', models.CharField(max_length=2000, verbose_name='Company name ')),
                ('company_name_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='اسم الشركة ')),
                ('locaction_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Location ')),
                ('locaction_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='الموقع ')),
                ('mobile_number', models.CharField(blank=True, default='', max_length=2000, verbose_name='رقم الموبايل / Phone number ')),
                ('email', models.EmailField(blank=True, default='', max_length=2000, verbose_name='البريد الاكتروني / Email ')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='image ')),
                ('image_ar', models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة ')),
                ('locaction_url', models.CharField(blank=True, default='', max_length=2000, verbose_name='Location url')),
            ],
            options={
                'verbose_name': 'Contact U',
            },
        ),
        migrations.CreateModel(
            name='ContactUSForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=2000, verbose_name='الاسم / First name ')),
                ('l_name', models.CharField(blank=True, default='', max_length=2000, verbose_name='الشهرة / Last name ')),
                ('mobile_number', models.CharField(blank=True, default='', max_length=2000, verbose_name='رقم الموبايل / Phone number ')),
                ('company_name', models.CharField(blank=True, default='', max_length=2000, verbose_name='اسم الشركة / Company name ')),
                ('work_email', models.EmailField(blank=True, default='', max_length=2000, verbose_name='البريد الاكتروني الخاص بالعمل / Work Email ')),
                ('message', models.TextField(blank=True, default='', max_length=2000, verbose_name='الرسالة / Message ')),
            ],
            options={
                'verbose_name': 'Contact Us Form',
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_in_home', models.BooleanField(default=False, verbose_name='تظهر في الصفخة الرئيسية ؟ / Show in home page ? ')),
                ('title_en', models.CharField(blank=True, max_length=2000, verbose_name='Title ')),
                ('title_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان ')),
                ('subtitle_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Subtitle ')),
                ('subtitle_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان الفرعي ')),
                ('text_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Text ')),
                ('text_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='النص ')),
                ('description_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Description ')),
                ('description_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='الوصف ')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Image ')),
                ('image_ar', models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة ')),
                ('test', models.CharField(blank=True, default='', max_length=2000, verbose_name='عنوان ')),
            ],
            options={
                'verbose_name': 'Hero',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='تظهر في الموقع / Show in webSite ? ')),
                ('ourPartners_title_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Title in our partner section ')),
                ('ourPartners_title_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان في مقطع شركائنا')),
                ('ourPartners_subtitle_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Subtitle in our partner section')),
                ('ourPartners_subtitle_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان الفرعي في مقطع شركائنا')),
                ('title_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Title in hero section ')),
                ('title_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان في القائمة الرئيسية')),
                ('subtitle_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Subtitle in hero section ')),
                ('subtitle_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان الفرعي في القائمة الرئيسية ')),
                ('text_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Text in hero section ')),
                ('text_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='النص في القائمة الرئيسية ')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='image in hero section ')),
            ],
            options={
                'verbose_name': 'Home Page',
            },
        ),
        migrations.CreateModel(
            name='OurServicesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_in_service_page', models.BooleanField(default=False, verbose_name='تظهر في صفحة الخدمات ؟ / Show in services page ? ')),
                ('title_en', models.CharField(max_length=2000, verbose_name='Title ')),
                ('title_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان ')),
                ('text_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Text ')),
                ('text_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='النص ')),
            ],
            options={
                'verbose_name': 'Our Services Page',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=2000, verbose_name='Title ')),
                ('title_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان ')),
                ('name_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Name ')),
                ('name_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='الاسم ')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة / Image ')),
            ],
            options={
                'verbose_name': 'Partner',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_in_service_page', models.BooleanField(default=False, verbose_name='تظهر في صفحة الخدمات ؟ / Show in services page ? ')),
                ('show_in_home', models.BooleanField(default=False, verbose_name='تظهر في الصفحة الرئيسية ؟ / Show in home page ? ')),
                ('title_en', models.CharField(max_length=2000, verbose_name='Title ')),
                ('title_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان ')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Image ')),
                ('image_ar', models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة ')),
                ('slug', models.SlugField(blank=True, verbose_name='المعرف / Slug ')),
            ],
            options={
                'verbose_name': 'Service',
            },
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=2000, verbose_name='Title ')),
                ('title_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان ')),
            ],
            options={
                'verbose_name': 'Our Value',
            },
        ),
        migrations.CreateModel(
            name='ListServiceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=2000, verbose_name='Title ')),
                ('title_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='العنوان ')),
                ('text_en', models.CharField(blank=True, default='', max_length=2000, verbose_name='Text ')),
                ('text_ar', models.CharField(blank=True, default='', max_length=2000, verbose_name='النص ')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='الصورة / Image ')),
                ('partners_id', models.ManyToManyField(blank=True, to='api.partners', verbose_name='العملاء / Partners ')),
                ('service_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.service', verbose_name='الخدمة /service ')),
            ],
            options={
                'verbose_name': 'List Service Detail',
            },
        ),
    ]