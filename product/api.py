# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from.serializers import ProductListSerilizer,ProductDetailSerilizer , BrandListSerilizer,BrandDetailSerilizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Product ,Brand
from rest_framework import generics






# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all() [:20] #list
#     data = ProductSerilizer(products,many=True,context={'request':request}).data  # تحول json
#     return Response({'products':data})




# @api_view(['GET'])
# def product_detail_api(request,product_id):
#     products = Product.objects.get(id =product_id) #list
#     data = ProductSerilizer(products,context={'request':request}).data  # تحول json
#     return Response({'product':data})



class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerilizer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtitle','description']
    ordering_fields = ['price', 'quantity']


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerilizer  





class BrandListAPI(generics.ListAPIView): 
    queryset = Brand.objects.all()
    serializer_class = BrandListSerilizer





class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerilizer
