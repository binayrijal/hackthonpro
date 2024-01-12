from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import service,service_name

# Create your views here.
def index(request):
 
    return render(request,'index.html')

def Contactus(request):
    return render (request,'contact_details.html')

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
    if request.method=="POST":
       formdata=request.POST.get('category')
       
       if formdata:
        selected_service = get_object_or_404(service, category=formdata)
        selected_servicename = service_name.objects.filter(service=selected_service)
        all_methods=[]
        for s in selected_servicename:
          splitmethod=s.methods.split(',')
          all_methods.extend(splitmethod)
          return render(request,'services.html',{'selected_service':selected_service,'selected_servicename':selected_servicename,'data':formdata,'all_methods':all_methods})
        
       else:
          JsonResponse("error in selected file")
          



    else:
     services=service.objects.all()
     all_service_names = service_name.objects.all()

    # Creating a list to hold methods from all service_name instances
    
     return render(request,'services.html',{
        'all_service_names':all_service_names,
        'services':services,
     })
    
   
