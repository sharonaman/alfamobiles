from django.http import HttpResponse
from django.shortcuts import render
#create function
def homePage(request):
    return render(request, "index.html")