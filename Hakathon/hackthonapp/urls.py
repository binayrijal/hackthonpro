from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm,UserPasswordResetForm

urlpatterns = [
    path('',views.index,name='index'),
    path('Aboutus/',views.Aboutus,name='Aboutus'),
    path('Contactus/',views.Contactus,name='Contactus'),
    path('services/',views.services,name='services'),
    path('Signup/',views.Signup,name='Signup'),
    path('profile/',views.profile,name='profile'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=UserLoginForm),name="loginuser"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password-reset.html',form_class=UserPasswordResetForm),name='password_reset'),

]
