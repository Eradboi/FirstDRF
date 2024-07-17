from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from products.models import Products

# using drf
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
#drf api view
# it requires allowed http methods
@api_view(['POST'])
def api_home(request, *args,**kwargs):
    # if we typically use our remote client to send  post request (request.post(;;;)), we will get a csrf token failure
    """
    Initial Practice
    body = request.body # byte string of Json 
    data = {}
    print(request.GET) # this give all query parameters
    try:
        data= json.loads(body) # converts Json to python dict
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type"""
    instance = Products.objects.all().order_by('?').first()
    data = {}
    if instance:
        """
        Insted of this
        data['id'] = instance.id
        data['title'] = instance.title
        data['about'] = instance.about
        data['price'] = instance.price"""
        # we can use drf model serializer instead of model_to_dict
        # sale_price will not show up at default
        #data = model_to_dict(instance, fields=['id','about','price','sale_price'])
        #data = ProductSerializer(instance).data
        
        serializer = ProductSerializer(data = request.data)
        # adding raise_exception in the is_valid method will give a detailed error
        if serializer.is_valid(raise_exception=True):
            #instance = serializer.save()
            #print(instance)
            print(serializer.data)
            return Response(serializer.data)
        return Response({'invalid':'not good data'})
    # we can use drf instead
    #return JsonResponse(data)


def home(request):
    return HttpResponse('<h1>WELCOME EJE MI</h1>')