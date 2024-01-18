from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html
class Hero(models.Model):
    show_in_home = models.BooleanField(default=False,verbose_name=u"تظهر في الصفخة الرئيسية ؟ / Show in home page ? ")
    title_en=models.CharField(max_length=255,verbose_name=u"Title ")
    title_ar=models.CharField(max_length=255, blank=True,default="",verbose_name=u"العنوان ")
    subtitle_en=models.CharField(max_length=255, blank=True,default="",verbose_name=u"Sub Title ")
    subtitle_ar=models.CharField(max_length=255, blank=True,default="",verbose_name=u"العنوان الفرعي ")
    text_en=models.CharField(max_length=255, blank=True,default="",verbose_name=u"Text ")
    text_ar=models.CharField(max_length=255, blank=True,default="",verbose_name=u"النص ")
    description_en=models.CharField(max_length=255, blank=True,default="",verbose_name=u"Description ")
    description_ar=models.CharField(max_length=255, blank=True,default="",verbose_name=u"الوصف ")
    image=models.ImageField(upload_to='images/',blank=True,verbose_name=u"Image ")
    image_ar=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الصورة ")
    
    def __str__(self):
        return self.title_en


class Values(models.Model):
   
    
    title_en=models.CharField(max_length=255,verbose_name=u"Title ")
    title_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان ")
   
    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Our Values'

class OurParnters(models.Model):
    title_en=models.CharField(max_length=255,verbose_name=u"Title ")
    title_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان ")
    subTitle_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Sub Title ")
    subTitle_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان الفرعي ")
    text_en=models.TextField(max_length=255,blank=True,default="",verbose_name=u"Text ")
    text_ar=models.TextField(max_length=255,blank=True,default="",verbose_name=u"النص ")
    image=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الصورة / Image ")
    logo=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الشعار / Logo ")
    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Our Parentes'    

# Create your models here.
class AboutUS(models.Model):
   
    active = models.BooleanField(default=False,verbose_name=u"تظهر في الموقع ؟ / Show in webSite ? ")
    aboutus_ar=models.TextField(max_length=255,verbose_name=u"About US ")
    aboutus_en=models.TextField(max_length=255,blank=True,default="",verbose_name=u"حولنا ")
    title_hero_en=models.TextField(max_length=255,blank=True,default="",verbose_name=u"Title")
    title_hero_ar=models.TextField(max_length=255,blank=True,default="",verbose_name=u"العنوان")
    subtitle_hero_en=models.TextField(max_length=255,blank=True,default="",verbose_name=u"Sub Title ")
    subtitle_hero_ar=models.TextField(max_length=255,blank=True,default="",verbose_name=u"العنوان الفرعي ")
    text_hero_en=models.TextField(max_length=255,blank=True,default="",verbose_name=u"Text ")
    text_hero_ar=models.TextField(max_length=255,blank=True,default="",verbose_name=u"النص ")
    image_hero=models.ImageField(upload_to='images/',blank=True,verbose_name=u"Image in section about us ")
    image_hero_ar=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الصورة في مقطع حولنا")
    
    ourParnters_id=models.ForeignKey(OurParnters, on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"شركتنا الأم / Our Parent Company ")
    title_our_partner_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Titel in Secion Our Partners ")
    title_our_partner_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان في مقطع جميع العملاء ")
    sub_title_our_partner_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Sub Titel in Secion Our Partners ")
    sub_title_our_partner_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان الفرعي في مقطع جميع العملاء ")

    title_our_vision_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Titel in Secion Our Vision ")
    title_our_vision_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان في مقطع رؤيتنا")
    text_our_vision_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Text in Secion Our Vision ")
    text_our_vision_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"النص في مقطع رؤيتنا")
    image_our_vision=models.ImageField(upload_to='images/',blank=True,verbose_name=u"Image in section our vision ")
    image_our_vision_ar=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الصورة في مقطع رؤيتنا ")
    title_our_values_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Titel in Secion Our Values ")
    title_our_values_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان في مقطع مبادئنا")
    def __str__(self):
        return self.aboutus_en
    
class Partners(models.Model):
    title_en=models.CharField(max_length=255,verbose_name=u"Title ")
    title_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان ")
    name_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Name ")
    name_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"الاسم ")
    image=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الصورة / Image ")

    def __str__(self):
        return self.title_en

        



class Service(models.Model):
    show_in_service_page = models.BooleanField(default=False,verbose_name=u"تظهر في صفحة الخدمات ؟ / Show in services page ? ")
    show_in_home = models.BooleanField(default=False,verbose_name=u"تظهر في الصفحة الرئيسية ؟ / Show in home page ? ")
    title_en =models.CharField(max_length=255,verbose_name=u"Title ")
    title_ar =models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان ") 
    
    
    image=models.ImageField(upload_to='images/',blank=True,verbose_name=u"Image ")   
    image_ar=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الصورة ")   
    slug=models.SlugField(blank=True,verbose_name=u"المعرف / Slug ")
    
    def __str__(self):
        return self.title_en
    def save(self, *args, **kwargs):
        if not self.slug or self.title_en != getattr(self, '_original_title_en', ''):
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)
        self._original_title_en = self.title_en 

class ListServiceDetails(models.Model):
    
    title_en=models.CharField(max_length=255,verbose_name=u"Title ")
    title_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان ")
    text_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Text ")
    text_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"النص ")
    image=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الصورة / Image ")
    service_id=models.ForeignKey(Service, on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"الخدمة /service ")
    partners_id = models.ManyToManyField(Partners, blank=True,verbose_name=u"العملاء / Partners ")
    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'List Service Details' 

class OurServicesPage(models.Model):
    
    show_in_service_page = models.BooleanField(default=False,verbose_name=u"تظهر في صفحة الخدمات ؟ / Show in services page ? ")
    title_en=models.CharField(max_length=255,verbose_name=u"Title ")
    title_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان ") 
    text_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Text ")  
    text_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"النص ") 
    
    
    def __str__(self):
        return self.title_en
    class Meta:
        verbose_name = 'Our services Page'





class AboutUsHero(models.Model):
    
    title_en=models.CharField(max_length=255,verbose_name=u"Title ")
    title_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان ")
    subtitle_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Sub Title ")
    subtitle_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان الفرعي  ")
    text_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Title ")
    text_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Title ")
    image=models.ImageField(upload_to='images/',blank=True,verbose_name=u"Title ")
    
    def __str__(self):
        return self.title_en
    def image_tag(self):
        return format_html('<img src="{}" width="50" height="50" />', self.image.url)

    image_tag.short_description = 'Image'


class HomePage(models.Model):
    
    
    active = models.BooleanField(default=False,verbose_name=u"تظهر في الموقع / Show in webSite ? ")
    ourPartners_title_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Title in our partner section ")
    ourPartners_title_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان في مقطع شركائنا")
    ourPartners_subtitle_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Sub title in our partner section")
    ourPartners_subtitle_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"العنوان الفرعي في مقطع شركائنا")
    about_hero_id=models.ForeignKey(AboutUsHero, on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"About Hero ")
    
class ContactUSForm(models.Model):
    f_name=models.CharField(max_length=255,verbose_name=u"الاسم / First name ")
    l_name=models.CharField(max_length=255,blank=True,default="",verbose_name=u"الشهرة / Last name ")
    mobile_number=models.CharField(max_length=255,blank=True,default="",verbose_name=u"رقم الموبايل / Phone number ")
    company_name=models.CharField(max_length=255,blank=True,default="",verbose_name=u"اسم الشركة / Company name ")
    work_email=models.EmailField(max_length=255,blank=True,default="",verbose_name=u"البريد الاكتروني الخاص بالعمل / Work Email ")
    message=models.TextField(max_length=255,blank=True,default="",verbose_name=u"الرسالة / Message ")
    def __str__(self):
        return self.f_name

class ContactUS(models.Model):
    active = models.BooleanField(default=False,verbose_name=u"تظهر في الموقع ؟ / Show in webSite ?  ")
    company_name_en=models.CharField(max_length=255,verbose_name=u"Company name ")
    company_name_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"اسم الشركة ")
    locaction_en=models.CharField(max_length=255,blank=True,default="",verbose_name=u"Location ")
    locaction_ar=models.CharField(max_length=255,blank=True,default="",verbose_name=u"الموقع ")
    mobile_number=models.CharField(max_length=255,blank=True,default="",verbose_name=u"رقم الموبايل / Phone number ")
    email=models.EmailField(max_length=255,blank=True,default="",verbose_name=u"البريد الاكتروني / Email ")
    image=models.ImageField(upload_to='images/',blank=True,verbose_name=u"الصورة / image ")
    locaction_image=models.ImageField(upload_to='images/',blank=True,verbose_name=u"صورة للموقع على الخريطة / Map in location ")
   
    
    def __str__(self):
        return self.company_name_en
