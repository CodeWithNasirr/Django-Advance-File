from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('Otp/<int:id>',views.Otp,name='otps'),
    path('Dash',views.dash,name='dash')
]