from django.shortcuts import render
from django .db.models import Count
from product.models import Product , Brand , Review



# Create your views here.





def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))
    sale_product = Product.objects.filter(flag = 'Sale')[:10]
    feature_product =  Product.objects.filter(flag = 'Feature')[:6]
    new_product =  Product.objects.filter(flag = 'New')[:10]
    reviews = Review.objects.all()[:5]



    return render(request,'setting/home.html',{
       'brands':brands,
       'sale_product':sale_product,
        'feature_product': feature_product,
         'new_product':new_product, 
         'reviews': reviews,
         
    })
