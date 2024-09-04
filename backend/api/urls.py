from django.urls import path,include
from .views import api_home,home
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', api_home,name='api'),
    path('home/',home,name='homepage'),
]