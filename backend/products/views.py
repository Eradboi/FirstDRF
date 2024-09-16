from django.shortcuts import render

# Create your views here.
# WE started with generic api views

from rest_framework import generics, mixins
from .models import Product
from api.mixins import StaffEditorPermissionMixin
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from django.shortcuts import get_object_or_404

# to change the keywork for the headers
from api.authentication import TokenAuthentication
class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    # somehow like class based views
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#A create api view
class ProductCreateAPIView(
    StaffEditorPermissionMixin,
    generics.CreateAPIView):
    # somehow like class based views
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Generally, a perfom_create function works on a post request while a queryset works on the get request
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        about = serializer.validated_data.get('about') or None
        print(title,about)
        if about is None:
            about = 'No description given'
        serializer.save(about=about)


# We will now be doing the update and delete views
class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView, generics.RetrieveUpdateAPIView):
    # somehow like class based views
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # difference with the detail view is the lookup field
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.about:
            instance.about = "Newest Shipping"
            serializer.save()

class ProductDeleteAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    # somehow like class based views
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # difference with the detail view is the lookup field
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)








# to list and create
class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    # somehow like class based views
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # we can add a permissions class
    # Ther are several authentication classes
    
    # We can add an authentication class
    #auth classes might be necessary if it is covered for 
    #authentication_classes = [authentication.SessionAuthentication,TokenAuthentication]
    def perform_create(self, serializer):
        """
        email = serializer.validated_data.pop('email')
        print(email)"""
        title = serializer.validated_data.get('title')
        about = serializer.validated_data.get('about') or None
        if about is None:
            about = 'No description given'
        serializer.save(about=about)

class ProductPatchAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




















# we add the mixin module from rest_framework also
class ProductMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin
                       ,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk =kwargs.get("pk")
        if  pk != None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    #vIn the situation where there are two post options: post and perform create, django picks perform create
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        about = serializer.validated_data.get('about') or None
        print(title,about)
        if about is None:
            about = f'This is the latest {title} on PurchaseMart'
        serializer.save(about=about)


# this is to combine the detailview, createview and listview.
# the problem with this view is that it is confusing
@api_view(['GET','POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method
    if method == 'GET':
        # This is the detail view
        if pk != None:
            object = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(object, many=False).data
            return Response(data)
        else:
            # HERE WE CREATE A LIST VIEW
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)

    if method == 'POST':
        serializer = ProductSerializer(data = request.data)
        # adding raise_exception in the is_valid method will give a detailed error
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            about = serializer.validated_data.get('about') or None
            print(title,about)
            if about is None:
                about = 'No description given'
            serializer.save(about=about)
            print(serializer.data)
            return Response(serializer.data)
        return Response({'invalid':'not good data'}, status=400)