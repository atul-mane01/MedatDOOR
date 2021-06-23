from django.contrib import admin
from .models import Appointment, Medicines, Signup, Medicines
# Register your models here.
admin.site.register(Signup)
admin.site.register(Appointment)
admin.site.register(Medicines)
