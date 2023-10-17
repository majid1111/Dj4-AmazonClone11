from rest_framework import serializers 

from .models import Cart , CartDetail ,Order , OrderDetail
from product.models import Product
from product.serializers import ProductCartSerializer



class CartDetailSerializer(serializers.ModelSerializer):
    product = ProductCartSerializer()
    # product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

