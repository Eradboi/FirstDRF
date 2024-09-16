from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    get(list),get(retrive),put,patch,post
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk'

class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    """
    to restrict the router url to two request types
    get(list),get(retrive)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk'