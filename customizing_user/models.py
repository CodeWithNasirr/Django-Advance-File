from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager



#Customizing User
class CustomUser(AbstractUser):
    username=models.CharField(max_length=100,null=True,blank=True)
    phone_number=models.FloatField(max_length=12,unique=True)
    profile_image=models.ImageField(upload_to="User/Profile")
    is_verify=models.BooleanField(default=False)

    USERNAME_FIELD="phone_number"
    REQUIRED_FIELDS=[]

    object=UserManager()

    def __str__(self):
        return str(self.phone_number)