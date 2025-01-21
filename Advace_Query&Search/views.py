from django.shortcuts import render
from .models import Student
from django.db.models import Q
from  django.http import HttpResponse
# Create your views here.
from test_study.forms import StudentForm
def Home(request):
    return render(request,'Dashboard/dashboard.html')

def Search(request): 
    student=Student.objects.all()
    search=request.GET.get('search').lower()
    age=request.GET.get('age')
    if search:
        student=student.filter(Q(name__icontains=search)|Q(Email__icontains=search) |Q(number__icontains=search) |Q(gender__icontains=search) |Q(collage__collage_name__icontains=search) )
        
    if age:
        if age =="1":
            student=student.filter(age__gte=18,age__lte=20).order_by('age')
        if age =='2':
            student=student.filter(age__gte=20,age__lte=22).order_by('age')
        if age =='3':
            student=student.filter(age__gte=22,age__lte=24).order_by('age')


    context={'students':student,'search':search,'age':age}
    return render(request,'Dashboard/search.html',context)



