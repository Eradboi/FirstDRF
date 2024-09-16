from rest_framework import serializers
from .models import Product


# validator function
def validate_title(value):
        qs = Product.objects.filter(title__exact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already there lil bro")
        return value