from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import GettingUser

from .forms import SignUp

# Create your views here.


def signUp(request):
    '''this method is for sign up users in app'''
    # return HttpResponse('Hello, World!')
    return render(request, 'getuser/index.html')


# TODO use forms in django


def signUp(request):
    if request.method == 'POST':
        form = signUp(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/welcome/')
    else:
        form = signUp()

    context = {
        'form': form,
    }
    return render(request, 'getuser/index.html', context)
