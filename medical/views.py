from django.http import request
from django.shortcuts import render,HttpResponse
from .models import Appointment, Medicines, Signup
# Create your views here.
def index(request):
    print("asvgvgsvcgc")
    if request.method == "POST":
        print("asbcjhaschbhjsabchjbsahbchjasbchjb")
        name=request.POST.get('name')
        date=request.POST.get('date')
        # department=request.POST.get('department')
        phone_no=request.POST.get('phone_no')
        # doctor=request.POST.get('doctor')
        email=request.POST.get('email')
        message=request.POST.get('message')
        ins=Appointment(email=email,name=name,date=date,phone_no=phone_no,message=message)
        ins.save()
    temp_name='index.html'
    return render(request,temp_name)
def signup(request):
    if request.method == "POST":
        print("asbcjhaschbhjsabchjbsahbchjasbchjb")
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        password=request.POST.get('password')
        phone_no=request.POST.get('phone_no')
        email=request.POST.get('email')
        data=Signup(first_name=first_name,last_name=last_name,address=address,city=city,state=state,zip=zip,password=password,phone_no=phone_no,email=email)
        data.save()
        
    temp_name='signup.html'
    print("hello")
    return render(request,temp_name)

def login(request):
    temp_name='examples/login.html'
    return render(request,temp_name)
   
def dashboard(request):
    data=Medicines.objects.all()

    temp_name='examples/dashboard.html'
    return render(request,temp_name,{'data':data})

def uploadprescription(request): 
    temp_name='examples/uploadprescription.html'
    return render(request,temp_name) 

def map(request): 
    temp_name='examples/map.html'
    return render(request,temp_name) 
def maps(request): 
    temp_name='examples/maps.html'
    return render(request,temp_name) 
def labtest(request): 
    temp_name='examples/labtest.html'
    return render(request,temp_name) 
def rtl(request): 
    temp_name='examples/rtl.html'
    return render(request,temp_name) 
def tables(request): 
    temp_name='examples/tables.html'
    return render(request,temp_name) 
def appointment(request): 
    temp_name='examples/appointment.html'
    return render(request,temp_name) 
def upgrade(request): 
    temp_name='examples/upgrade.html'
    return render(request,temp_name) 
def user(request): 
    data=Signup.objects.all()
    print(data)
    temp_name='examples/user.html'
    return render(request,temp_name,{'data':data}) 