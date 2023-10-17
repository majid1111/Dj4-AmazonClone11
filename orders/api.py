from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from.serializers import CartSerializer
from.models import Cart ,CartDetail
from product.models import Product



class CartDetailCreateAPI(generics.GenericAPIView):
    serializer_class = CartSerializer



    def get(self,request,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart, created = Cart.objects.get_or_create(user = user,status='InProgress')
        data = CartSerializer(cart).data
        return Response({'cart':data})
    
    def post(self,request,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        product = Product.objects.get(id = request.data['product_id'])
        quantity = int(request.data['quantity'])
        cart = Cart.objects.get(user = user,status='InProgress')
        cart_detail , created =CartDetail.objects.get_or_create(cart =cart,product = product)
        cart_detail.quantity= quantity
        cart_detail.total = round(quantity*product.price,2)
        cart_detail.save()
        cart = Cart.objects.get(user = user,status='InProgress')
        data = CartSerializer(cart).data
        return Response({'messsage':'product added successfully','cart':data})


    def delete (self,request,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart_detail = CartDetail.objects.get(id =request.data['cart_detail_id'])
        cart_detail.delete()

        cart = Cart.objects.get(user = user,status='InProgress')
        data = CartSerializer(cart).data
        return Response({'messsage':'product deleted successfully','cart':data})