from django.shortcuts import render

from .models import Tatuagem

def lista_tatuagens(request):
    tatuagens = Tatuagem.objects.all()
    return render(request, "tatuagens.html", {"tatuagens": tatuagens})

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html') 
