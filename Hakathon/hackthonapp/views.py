from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import service_name,service,feedback
from django.contrib.auth.models import User


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
       if formdata:
        print(formdata)
        selected_servicename = service_name.objects.filter(name=formdata)
        all_methods=[]
        for s in selected_servicename:
          splitmethod=s.methods.split(',')
          all_methods.extend(splitmethod)
          return render(request,'services.html',{'selected_servicename':selected_servicename,'data':formdata,'all_methods':all_methods})
        
       else:
          return JsonResponse({"error":"error in selected file"},safe=False)
          



    else:
     all_service_names = service_name.objects.all()

    # Creating a list to hold methods from all service_name instances
    

     return render(request,'services.html',{
        'all_service_names':all_service_names,
        'services':services,
     })
    
   
def feedbackuser(request):
    if request.method=="POST":
       user=request.POST.get('user')
       email=request.POST.get('email')
       service=request.POST.get('service')
       phone=request.POST.get('phone')
       message=request.POST.get('message')

       if User.objects.filter(email=email).exists():
          feedback_message=feedback.objects.create(user=user,email=email,service_name=service,phone=phone,message=message)
          feedback_message.save()

          if service==service_name.category:
           
           return render(request,'feedback.html',{'feedback':feedback_message,'service':service})
          
          else:
             
             return render(request,'feedback.html',{'error':'service name select properly'})
          
       else:
           #yeslai jaha yo form ma click garera jaha action xa tya print garne

           messages.success(request,'user doesnot exist')
       

       

          
    
          
       

       
=======
    return render (request,'services.html')

from django.shortcuts import render
from gtts import gTTS

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        language = 'en'  # Set the language code accordingly

        tts = gTTS(text=text, lang=language, slow=False)
        tts.save('tts_app/static/tts_app/output.mp3')  # Save the TTS audio file

        return render(request, 'tts_app/index.html', {'audio_path': 'static/tts_app/output.mp3'})

    return render(request, 'tts_app/index.html')
>>>>>>> 31ae614afcbaabb3c0fb1cf25a74f1d76c6a61a7
