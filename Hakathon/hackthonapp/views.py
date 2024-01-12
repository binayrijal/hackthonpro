from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from .models import service,service_name
from django.http import HttpResponse,JsonResponse

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
       formdata=request.POST.get('search')
       print(formdata)
       if formdata:
        selected_service = get_object_or_404(service, category=formdata)
        selected_servicename = service_name.objects.filter(service=selected_service)
        servicename=service_name.objects.get(id=formdata)
        all_methods=[]
        if servicename.methods:
            splitmethod=servicename.methods.split(',')
            all_methods.extend(splitmethod)
            data={
               'all_methods':all_methods
            }
            return JsonResponse(data)
        else:
            return JsonResponse("error")
       else:
         return render(request,'service.html')
        
        
    else:
          return HttpResponse("no data is selected")





    # Creating a list to hold methods from all service_name instances
    
     
