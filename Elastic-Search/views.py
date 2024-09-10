from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .emails import Send_Otp
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
# from django.contrib.postgres.search import TrigramSimilarity
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from accounts.documents import ProductDocument
from elasticsearch_dsl.query import MultiMatch 


def search_pdts(request):
    data={
        'Status':False,
        'Prodcuts':[]
    }
    if request.GET.get('search'):
        search=request.GET.get('search').split(' ' or ',')#split only for terms
        print(search)
        result=ProductDocument.search().query(

            # 'match',Title=search # iam a boy ager sentence pe kahi per boy ayega to ye return kardega
            # 'term',brand_names__brand_name = search#Term excatly same name pe work karta ha 
            # 'match',Title={ #This is for Furzziness 
            #     'query' : search,
            #     'fuzziness':"AUTO"
            # }
            # MultiMatch(query=search,fields=[
            #     'Title',
            #     'Description',
            #     'Category',
            #     # 'Price',
            #     'brand',
            #     'SKU',
            #     'Score'
            # ])).extra(size=20).collapse(field='Price')
            # 'terms',brand_names__brand_name=search #Terms use kaam ayta ha jab muje duble brand 1sath bulna padta ha
            )
            
        result=result.execute()
        data['Status']=True
        Products=[{
                'Title':x.Title,
                'Description':x.Description,
                'Category':x.Category,
                'Price':x.Price,
                'brand':x.brand,
                'SKU':x.SKU,
                'Score':x.meta.score
            }for x in result]
        data['Prodcuts']=Products
    return JsonResponse(data)