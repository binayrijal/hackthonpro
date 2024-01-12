from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import service_name

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

def update_service_names(request):
    try:
        service_name.update_with_latest_updates()
        message = "Service names updated successfully."
    except Exception as e:
        # Log the error, notify administrators, or handle it appropriately
        message = f"Error updating service names: {e}"

    return render(request, 'update_result.html', {'message': message})