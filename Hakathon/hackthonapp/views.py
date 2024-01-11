from django.shortcuts import render


# Create your views here.
def index(request):
 
    return render(request,'index.html')

def Contactus(request):
    return render (request,'Contactus.html')

def Aboutus(request):
    return render (request,'Aboutus.html')

def Signup(request):
    return render (request,'Signup.html')

def profile(request):
    return render (request,'profile.html')

def services(request):
    return render (request,'services.html')
