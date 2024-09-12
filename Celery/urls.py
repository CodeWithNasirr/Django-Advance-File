from django.urls import path,include
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls
urlpatterns=[
    # path('search/',views.search_pdts,name='searchs')
     path('',views.search,name='searchs'),
     path('results/<str:id>/',views.search_result,name='Check_Results')
     
]+ debug_toolbar_urls()