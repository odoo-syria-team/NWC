from django.urls import path
from .views import HeroListAPIView,OurParntersApiView,ValuesApiView,ServiceApiView,AboutUSApiView,HomePageApiView,ServiceItemApiView,ContactUSApiView,ContactUSFormApiView,PartnersApiView
urlpatterns = [
    
    path('our_parnters/', OurParntersApiView.as_view(), name='our_parnters-list'),
    path('service/', ServiceApiView.as_view(), name='service-list'),
    path('service/<str:slug>/', ServiceItemApiView.as_view(), name='service_item-list'),
    path('about_us/', AboutUSApiView.as_view(), name='about_us-list'),
    path('home_page/', HomePageApiView.as_view(), name='home_page-list'),
    path('contact_us/', ContactUSApiView.as_view(), name='contact_us-list'),
    path('contact_us/form/', ContactUSFormApiView.as_view(), name='contact_us_form-list'),
    path('partners/', PartnersApiView.as_view(), name='partners-list'),
    
]