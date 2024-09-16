from django.urls import path,include
from .views import *
#from .views import api_view,home
urlpatterns = [
    path('<int:pk>/',ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update',ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete',ProductDeleteAPIView.as_view()),
    path('',ProductListCreateAPIView.as_view()),
    path('<int:pk>/put',ProductPatchAPIView.as_view())
]