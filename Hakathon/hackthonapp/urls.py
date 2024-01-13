from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm,UserPasswordResetForm,MySetPasswordForm


urlpatterns = [
    path('',views.index,name='index'),
    path('base/',views.base,name="base"),
    path('Aboutus/',views.Aboutus,name='Aboutus'),
    path('Contactus/',views.Contactus,name='Contactus'),
    path('contactdetails',views.contactdetails,name="contact"),
    path('feedback/',views.feedbackuser,name="feedback"),
    path('Signup/',views.Signup,name='Signup'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=UserLoginForm),name="loginuser"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=UserPasswordResetForm),name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'),name='password_reset_complete'),
    path('services/',views.services,name='services'),
    path('select_service/<slug:data>',views.select_service,name='select_services'),
    
]
