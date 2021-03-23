from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

# from .models import GettingUserData

# from .forms import SignUpForm

# Create your views here.


# just show a site without form
# def signUp(request):
#     '''this method is for sign up users in app'''
#     # return HttpResponse('Hello, World!')
#     return render(request, 'getuser/index.html')


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Hello user")

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'getuser/index.html', context)
