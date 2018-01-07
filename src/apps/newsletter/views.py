from django.shortcuts import render
from .models import dadosHome

from django.contrib.sitemaps import Sitemap


def home(request):
    info = dadosHome.objects.all()
    return render(request, 'home.html', {'info': info})


class dadosHomeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return dadosHome.objects.all()

    def lastmod(self, obj):
        return obj.data_modificacao
