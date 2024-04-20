
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,"index.html")


def getProduct(request,pid):
    
    return HttpResponse("I am id based URL "+str(pid))