from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

urlpatterns = [
    path('',views.index,name='index'),
    path('Aboutus/',views.Aboutus,name='Aboutus'),
    path('Contactus/',views.Contactus,name='Contactus'),
    path('services/',views.services,name='services'),
    path('Signup/',views.Signup,name='Signup'),
    path('profile/',views.profile,name='profile'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=UserLoginForm),name="loginuser"),

]
