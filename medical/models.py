from django.db import models
from django.db.models.fields import *

# Create your models here.
class Signup(models.Model):
    first_name=models.CharField(max_length=25,null=True,blank=True)
    last_name=models.CharField(max_length=25,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=25,null=True,blank=True)
    state=models.CharField(max_length=25,null=True,blank=True)
    zip=models.IntegerField()
    password=models.CharField(max_length=10,null=True,blank=True)
    phone_no=models.IntegerField()
    email=models.EmailField(max_length=25,null=True,blank=True)

    
class Appointment(models.Model):
    name=models.CharField(max_length=25,null=True,blank=True)
    email=models.EmailField(max_length=25,null=True,blank=True)
    phone_no=models.IntegerField()
    date=models.DateField()
    # department=models.CharField(max_length=25)
    # doctor=models.CharField(max_length=25)
    message=models.CharField(max_length=500,null=True,blank=True)

class Medicines(models.Model):
    med_id=IntegerField(primary_key=0)
    med_name=models.CharField(max_length=50)
    med_price=models.IntegerField()
    med_discount=models.IntegerField()
    med_description=models.CharField(max_length=100)


    
