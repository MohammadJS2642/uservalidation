from django.urls import path
from .views import *

urlpatterns=[
    path('', myMainPage, name='mainpage'),
]
