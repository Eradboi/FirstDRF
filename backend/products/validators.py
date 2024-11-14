from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

# validator function
def validate_title(value):
        qs = Product.objects.filter(title__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already exists")
        return value

def validate_title_no_swear(value):
    for x in ['fuck','shit','cunt','nigga','motherfucker']:
        if x in value.lower():
            raise serializers.ValidationError(f"{x} is a censored word")

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')