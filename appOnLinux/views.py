from django.http import HttpResponse
from django.shortcuts import render

def pierwsza(request):
    return render(request, "index.html", {"test": "heheszki"})

def druga(request):
    return HttpResponse("Witam")