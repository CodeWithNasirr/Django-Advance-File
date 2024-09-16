from django.shortcuts import render
from .models import Student
from django.db.models import Q
from  django.http import HttpResponse
# Create your views here.
from test_study.forms import StudentForm

def Home(request):
    context={'form':StudentForm}
    if request.method =="POST":
        data=StudentForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request,'Dashboard/forms.html',context)
