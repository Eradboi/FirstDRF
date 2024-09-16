from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title
class ProductSerializer(serializers.ModelSerializer):
    # to change the name of an object's item
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url =serializers.HyperlinkedIdentityField(view_name='product-detail',
                                              lookup_field='pk')
    #email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
            #'email',
            'url',
            'edit_url',
            'pk',
            'title',
            'about',
            'price',
            'sale_price',
            'my_discount',
        ]
        #validators
    """def validate_title(self, value):
        qs = Product.objects.filter(title__exact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already there eje")
        return value"""
    
    """def create(self, validated_data):
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        print(email, obj)
        return obj"""
    def get_edit_url(self, obj):
        #using the basic method
        #return f'api/products/{obj.pk}/'

        #using reverse
        # serializers don't alway have the request, this depends on the context that you give it.
        # those we did inside generic views will have a request

        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.discount()