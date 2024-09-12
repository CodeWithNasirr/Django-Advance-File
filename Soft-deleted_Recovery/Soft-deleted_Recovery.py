from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify
from test_study.utils import generate_slug


# Publisher Model
class CategoryManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted=False)

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=200)
    is_deleted=models.BooleanField(default=False)
    objects=CategoryManager()#Category.objects.all()This cmd only for get the Category details which on your Database
    NewManager=models.Manager()#Category.NewManager.all() This cmd for all Category Show Either Deleted Nor Not Deleted
    def __str__(self):
        return f"{self.name} Id: {self.id}{self.is_deleted}"

## Script.py 

def bulk_update_is_deleted():
    # Get the primary keys of the first 50 categories
    category_ids = Category.objects.values_list('id', flat=True)[:5]
    print(category_ids)
    # # Perform the bulk update using the retrieved primary keys
    updated_count = Category.objects.filter(id__in=category_ids).update(is_deleted=True)
    print(f"Updated {updated_count} categories as deleted.")


def bulk_update_for_Recover():
    # Retrieve the IDs of the categories that are marked as deleted
    category_ids = Category.NewManager.filter(is_deleted=True).values_list('id', flat=True)
    print(f"Recovered IDs: {list(category_ids)}")
    # Perform the bulk update to recover (set is_deleted=False)
    updated_count = Category.NewManager.filter(id__in=category_ids).update(is_deleted=False)
    
    # Print the IDs of the categories that were recovered
    print(f"Updated {updated_count} categories as Recovery. ")
