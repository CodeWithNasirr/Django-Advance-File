from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .emails import Send_Otp
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
import random
from .models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.contrib.postgres.search import TrigramSimilarity
import time
def search(request):
    if request.method == "POST":
        pdt=[]
        search = request.POST.get('search', "")
        if search:
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
        else:
            pdt=Products.objects.all()

    context = {"Products": pdt, 'search': search}
    return render(request, 'account/search.html', context)