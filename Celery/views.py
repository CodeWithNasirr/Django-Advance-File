from django.shortcuts import render,redirect
from celery.result import AsyncResult

from accounts.task import *

def search(request):
    results=add.delay(10,2)
    print(f"Celery Results: {results}")
    print(f'Success: {results.successful()}')
    context={"result":results}
    return render(request, 'account/search.html',context)
def search_result(request,id):
    results=AsyncResult(id)
    print(f'Success: {results.successful()}')
    return render(request,"account/results.html",{'result':results})