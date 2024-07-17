from django.urls import path,include
from .views import api_home,home
urlpatterns = [
    path('api/', api_home,name='api'),
    path('',home,name='homepage'),
]