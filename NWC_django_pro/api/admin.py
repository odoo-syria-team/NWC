from django.contrib import admin
# from django.contrib.admin import AdminSite
from .models import Hero,Values,OurParnters,AboutUS,Service,OurServicesPage,HomePage,AboutUsHero,Partners,ContactUS,ContactUSForm,ListServiceDetails
# Register your models here.




class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['aboutus_en', 'aboutus_ar','active']

class AboutUsHeroAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_ar','image_tag']

class ContactUSFormAdmin(admin.ModelAdmin):
    list_display = ['f_name', 'l_name','mobile_number']

class ContactUSAdmin(admin.ModelAdmin):
    list_display = ['company_name_en', 'company_name_ar','active'] 

class HeroAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_ar','show_in_home'] 

class HomePageAdmin(admin.ModelAdmin):
    list_display = ['active'] 

class OurParntersAdmin(admin.ModelAdmin):
    list_display = ['title_en','title_ar'] 

class ServiceAdmin(admin.ModelAdmin):
    # list_display = ['title_en','title_ar','service_id']  
    list_display = ['title_en','title_ar','show_in_service_page']

class OurServicesPageAdmin(admin.ModelAdmin):
    # list_display = ['title_en','title_ar','show_in_home','show_in_service_page']      
    list_display = ['title_en','title_ar']

class ValuesAdmin(admin.ModelAdmin):
    list_display = ['title_en','title_ar']  

class ListServiceDetailsِAdmin(admin.ModelAdmin):
    list_display = ['title_en','title_ar']      


admin.site.register(AboutUS, AboutUsAdmin)

    

admin.site.register(Hero,HeroAdmin)

admin.site.register(Values,ValuesAdmin)
admin.site.register(ListServiceDetails,ListServiceDetailsِAdmin)
admin.site.register(OurParnters,OurParntersAdmin)



admin.site.register(Service,ServiceAdmin)

admin.site.register(OurServicesPage,OurServicesPageAdmin)

admin.site.register(HomePage,HomePageAdmin)
admin.site.register(AboutUsHero,AboutUsHeroAdmin)
admin.site.register(Partners)
admin.site.register(ContactUS,ContactUSAdmin)

admin.site.register(ContactUSForm,ContactUSFormAdmin)
