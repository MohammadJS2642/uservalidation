from django.shortcuts import render

# Create your views here.
def myMainPage(request):
    return render(request, 'mainpage/index.html')
