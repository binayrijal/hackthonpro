from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages

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