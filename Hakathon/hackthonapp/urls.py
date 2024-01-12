from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm,UserPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('',views.index,name='index'),
    path('Aboutus/',views.Aboutus,name='Aboutus'),
    path('Contactus/',views.Contactus,name='Contactus'),
    
    path('Signup/',views.Signup,name='Signup'),
    path('profile/',views.profile,name='profile'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=UserLoginForm),name="loginuser"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=UserPasswordResetForm),name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('services/',views.services,name='services'),
]
