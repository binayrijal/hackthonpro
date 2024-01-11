from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('Passport','Passport'),
    ('Transportation','Transportation'),
    ('NEB','NEB'),
    ('ward','ward'),
    ('Municipality','Municipality'),
    ('Dist_office','Dist_office'),
    ('HighCourt','HighCourt'),
    ('DistCourt','DistCourt'),

)

class service(models.Model):
   category=models.CharField(choices=CATEGORY_CHOICES,max_length=100)

   
   def __str__(self):
       return self.category


class service_name(models.Model):
    
    service=models.ForeignKey(service,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    methods=models.TextField()

    def __str__(self):
        return self.name