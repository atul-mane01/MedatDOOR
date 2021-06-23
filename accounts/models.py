from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdetail")
    first_name=models.CharField(max_length=25,null=True,blank=True)
    last_name=models.CharField(max_length=25,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=25,null=True,blank=True)
    state=models.CharField(max_length=25,null=True,blank=True)
    zip=models.IntegerField()
    password=models.CharField(max_length=10,null=True,blank=True)
    phone_no=models.IntegerField()
    email=models.EmailField(max_length=25,null=True,blank=True)

    def __str__(self):
        return str(self.user.username)
