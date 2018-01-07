from .models import dadosHome, Imagem

from django.contrib.sitemaps import Sitemap


class dadosHomeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return dadosHome.objects.all()

    def lastmod(self, obj):
        return obj.data_modificacao


class imagemSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return Imagem.objects.all()

    def lastmod(self, obj):
        return obj.data
