from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .emails import Send_Otp
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.
import random
User=get_user_model()

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        user_obj=User.objects.filter(email=email)
        if not user_obj.exists():
            return redirect('/')
        email=user_obj[0].email
        otp=random.randint(1000,9999) 
        user_obj.update(otp=otp)
        subject='OTP for Login'
        message=f"Your Otp is {otp}"
        Send_Otp(email,subject,message)
        return redirect(f'Otp/{user_obj[0].id}')
    return render(request,"account/login.html")

def Otp(request,id):
    if request.method =='POST':
        otp=request.POST.get('otp')
        user_obj = User.objects.filter(id=id)[0] # Get the first user object
        if int(otp) == user_obj.otp:
            auth_login(request, user_obj)  # Use Django's login function
            return redirect('dash')
        else:
            print('Error: OTP does not match')

    return render(request,"account/otp_page.html")


@login_required(login_url='/')
def dash(request):
    return HttpResponse('You are logged in')