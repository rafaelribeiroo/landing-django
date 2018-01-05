from django.urls import path
from .views import (
    home,
)

app_name = 'newsletter'
urlpatterns = [
    path('', home, name='homepage'),
]
