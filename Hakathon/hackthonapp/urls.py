from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Aboutus/',views.Aboutus,name='Aboutus'),
    path('Contactus/',views.Contactus,name='Contactus'),
    path('services/',views.services,name='services'),
    path('Signup/',views.Signup,name='Signup'),
    path('profile/',views.profile,name='profile'),

]
