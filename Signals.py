from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver

class Student(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=10,choices=(('Male',"Male"),('Female',"Female")),null=True,blank=True)
    student_id=models.CharField(max_length=100,null=True,blank=True)

@receiver(post_save,sender=Student)
def save_student(sender,instance , created , **kwargs):
    print(sender,f"Name: {instance.name} Gender: {instance.gender}")
    if created:
        instance.student_id=f"STU-000{instance.id}"
        instance.save()
        print("Student Objects Created.... ")


@receiver(pre_delete, sender=Student)
def pre_delete_student(sender, instance, **kwargs):
    print(f'Deleted Item (Before Deletion) Name: {instance.name}')

@receiver(post_delete, sender=Student)
def post_delete_student(sender, instance, **kwargs):
    print(f'Deleted Item (After Deletion) Name: {instance.name}')