from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


import requests
from bs4 import BeautifulSoup

# Create your models here.
CATEGORY_CHOICES=(
    ('Passport','Passport'),
    ('Transportation','Transportation'),
    ('Citizenship','Citizenship'),
    ('Municipality','Municipality'),
   

)

class service(models.Model):
   category=models.CharField(choices=CATEGORY_CHOICES,max_length=100)

   
   def __str__(self):
       return self.category



class service_name(models.Model):
    id=models.IntegerField(primary_key=True)
    category=models.ForeignKey(service,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    methods=models.TextField()

    def __str__(self):
        return self.name
    

class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    service_name=models.ForeignKey(service_name,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', 'Phone number must be 10 digits')])
    Date = models.DateTimeField(auto_now_add=True)
    message=models.TextField(max_length=200)


    