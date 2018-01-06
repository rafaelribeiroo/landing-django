from django.shortcuts import render
from .models import dadosHome


def home(request):
    info = dadosHome.objects.all()
    return render(request, 'home.html', {'info': info})
