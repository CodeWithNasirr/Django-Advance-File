from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver
import os
from PIL import Image
class Image_Generater(models.Model):
    orginal_image=models.ImageField(upload_to="Images",null=True,blank=True)
    thumbnail_small=models.ImageField(upload_to="Images/thub",null=True,blank=True)
    thumbnail_medium=models.ImageField(upload_to="Images/thub",null=True,blank=True)
    thumbnail_large=models.ImageField(upload_to="Images/thub",null=True,blank=True)


@receiver(post_save,sender=Image_Generater)
def create_thub(sender,instance , created , **kwargs):
    print(instance.orginal_image.name)
    if created:
        sizes = {
            'thumbnail_small':(100,100),
            'thumbnail_medium':(300,300),
            'thumbnail_large':(600,600),
        }

    for fields, size in sizes.items(): 
        img = Image.open(instance.orginal_image.path)
        img.thumbnail(size, Image.Resampling.LANCZOS)
        if img.mode=='RGBA':
            img=img.convert('RGB')
        # Get the base name and extension correctly
        file_name,file_exten=os.path.splitext(os.path.basename(instance.orginal_image.name))
        # print(file_exten)  # This will print something like '.jpg'
        # print(file_name)       # This will print the base file name like 'example'

        # Create the new file name for the thumbnail
        thub_fileName = f"{file_name}_{size[0]}X{size[1]}{file_exten}"
        thub_path = f"thubnails/{thub_fileName}"

        # Save the thumbnail
        img.save(os.path.join(os.path.dirname(instance.orginal_image.path), thub_path))
        print(os.path.join(os.path.dirname(instance.orginal_image.path), thub_path))

        # Update the respective field in the model instance
        setattr(instance, fields, thub_path)