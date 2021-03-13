from django.shortcuts import render, HttpResponse
from .models import GettingUser


# Create your views here.
def signUp(request):
    '''this method is for sign up users in app'''
    # return HttpResponse('Hello, World!')
    return render(request, 'index.html')
