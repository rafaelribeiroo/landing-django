"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Habilitar MEDIA
from django.conf import settings
from django.conf.urls.static import static

# Multiplas URLS
from src.apps.newsletter import urls as newsletter_urls

# Sitemaps, SEO
from django.contrib.sitemaps.views import sitemap
from src.apps.newsletter.views import dadosHomeSitemap

sitemaps = {
    'post': dadosHomeSitemap,
}


app_name = 'core'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(newsletter_urls, namespace='core')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Utilizado para servir as midias do projeto
