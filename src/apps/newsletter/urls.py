from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import (
    home,
)

app_name = 'newsletter'
urlpatterns = [
    path('', home, name='homepage'),
    path('froala_editor/', include('froala_editor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
