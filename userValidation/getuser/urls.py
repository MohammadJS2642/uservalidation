from django.urls import path
from .views import signUp


app_name = 'getuser'
urlpatterns = [
    path('', signUp, name='signup')
]
