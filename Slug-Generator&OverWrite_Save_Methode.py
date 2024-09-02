from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify
from test_study.utils import generate_slug

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    slug=models.SlugField(max_length=100,blank=True,null=True)

    def save(self,*arags,**kwargs) -> None:
        if not self.slug:
            self.slug = generate_slug(self.name,Product)
            print("Working")
        return super().save(*arags,**kwargs)
    
    def __str__(self) -> str:
        return f"{self.name} id: {self.id}"
    
#Script.py

from django.template.defaultfilters import slugify
import uuid

def generate_slug(name,Product):
    new_slug=slugify(name)
    if Product.objects.filter(slug=new_slug).exists():
        # new_slug=f"{new_slug}-{str(uuid.uuid4()).split('-')[0]}"
        new_slug=f"{new_slug}-{str(uuid.uuid4())}"
        print(new_slug)
    return new_slug

