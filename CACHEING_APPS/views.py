from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .emails import Send_Otp
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.views.decorators.cache import cache_page
from django.core.cache import cache



def search(request):
    print('Successfully.....')
    if request.method == "GET":
        search = request.GET.get('search', "")
        if search:
            search_query=f"Search_{search}"
            pdt=cache.get(search_query)
            if pdt:
                print("DATA FROM CACHE")
            else:
                query = SearchQuery(search)
                vector = (SearchVector('Title', weight='A') +
                            SearchVector('Description', weight='B') +
                            SearchVector('Category', weight='C') +
                            SearchVector('SKU', weight='D'))
                rank = SearchRank(vector, query)
                pdt = Products.objects.annotate(
                        rank=rank,
                        # similarity=TrigramSimilarity('Title', search)
                    ).filter(rank__gte=0.3).order_by('-rank')
                cache.set(search_query,pdt,60*1)
                print("DATA FROM CACHE")
        else:
            cache_ex = "All Product"
            pdt=cache.get(cache_ex)
            if pdt:
                print('CACHE FROM CACHE')
            else:
                pdt=Products.objects.all()
                cache.set(cache_ex,pdt,60*1)
                print('CACHE FROM DB')
        context = {"Products": pdt, 'search': search}
        return render(request, 'account/search.html', context)