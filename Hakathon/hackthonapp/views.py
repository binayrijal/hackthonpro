from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages


# Create your views here.
def index(request):
 
    return render(request,'index.html')

def Contactus(request):
    return render (request,'Contactus.html')

def Aboutus(request):
    return render (request,'Aboutus.html')

def Signup(request):
 if request.method=="POST":
  form=UserRegistrationForm(request.POST)
  if form.is_valid():
     form.save()
     return redirect('loginuser')
     
 else:
  form=UserRegistrationForm()

 return render(request, 'Signup.html',{
  'form':form,
 })

def profile(request):
    return render (request,'profile.html')

def services(request):
    return render (request,'services.html')
