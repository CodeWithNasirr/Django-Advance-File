import requests
from accounts.models import Products
import json


# url='https://dummyjson.com/products?limit=500'
# response=requests.get(url)
# data=response.json()
# print(data)
# for pdt in data['products']:
#     x= Products.objects.create(
#         Title=pdt['title'],
#         Description=pdt['description'],
#         Category=pdt['category'],
#         Price=pdt['price'],
#         Brand=pdt.get('brand', 'Unknown'),
#         SKU=pdt["sku"],
#         Thubnails=pdt['thumbnail'],
#     )
# print('Data Update Successfully..')


#For Duplicate id Deleted
# from django.db.models import Count
# duplicates=Products.objects.values('Title').annotate(count=Count('id')).filter(count__gte=1)
# for x in duplicates:
#     print(f"Title {x['Title']}Total Count {x['count']}")
# for x in duplicates:
    # instance=Products.objects.filter(Title = x['Title'])
    # instance.exclude(id=instance.first().id).delete()
