from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify
from test_study.utils import generate_slug
# Create your models here.


class Collage(models.Model):
    collage_name=models.CharField(max_length=100)
    collage_address=models.CharField(max_length=1000)

    def __str__(self): 
        return self.collage_name
    
class Student(models.Model):
    collage=models.ForeignKey(Collage,on_delete=models.CASCADE,null=True,blank=True)
    gender_choice=(("Male","male"),("Female",'female'),('Other',"other"))
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=12)
    age=models.CharField(max_length=10,null=True,blank=True)
    Email=models.EmailField()
    gender=models.CharField(max_length=20,choices=gender_choice,default='Male')

    def __str__(self):
        return f"Student Name: {self.name} Age: {self.age}"

    # class Meta:
    #     ordering=('age','name')
    #     index_together=('age','name')
