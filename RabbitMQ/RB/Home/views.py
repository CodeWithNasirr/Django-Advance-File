from django.shortcuts import render
from django.http import HttpResponse
from Home.RabbitMQ import publish_msg
# Create your views here.
import random
from faker import Faker
fake=Faker()

def index(request):
    message=f'This is a demo message {random.randint(1,100)}'
    # names = [{'name':fake.name(),'address':fake.address()} for _ in range(0,10)]
    names=[]
    for i in range(0,10):
        name=fake.name()
        address=fake.address()
        names.append((name,address))
    publish_msg(names)
    return HttpResponse("Hello World")
    # return (request,'Home/index.html')
    


