from django.contrib import admin
from .models import service,service_name,feedback

# Register your models here.
admin.site.register(service)
admin.site.register(service_name)
admin.site.register(feedback)
