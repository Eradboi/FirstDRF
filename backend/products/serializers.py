from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    # to change the name of an object's item
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Products
        fields = [
            'title',
            'about',
            'price',
            'sale_price',
            'my_discount',
        ]
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Products):
            return None
        return obj.discount()