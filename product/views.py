from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django .views.generic import ListView ,DetailView
from . models import Product , Brand , Review , ProductImages
from django.db.models import Q ,F , Value
from django.db.models.aggregates import Max , Min , Count , Avg , Sum


from django.http import JsonResponse
from django.template.loader import render_to_string


def queryst_debug(request):
                                 #ممكن استخدم بدل all ب filter
    #data = Product.objects.select_related('brand').all()  #ممكن اعمل نفس العمليه عن طريق prefetch_related لكن هذا استخدمها عندما تكون العلاقه many-to-many
    #data = Product.objects.filter(price__gt=70) اكبر
    #data = Product.objects.filter(price__gte=70) اكبر يساوي
    #data = Product.objects.filter(price__lt=70) #اقل
    #data = Product.objects.filter(price__lte=70)#اقل او يساوي
    #data = Product.objects.filter(price__range=(60,70))


    #nvigate relation
    #data = Product.objects.filter(brand__name='Apple')
    #data = Product.objects.filter(brand__price__gt=20)


    # filter text
    # data = Product.objects.filter(name__contains='Brown')
    #data = Product.objects.filter(name__startswith='e')#يبدا وينتهي 
    #data = Product.objects.filter(name__endswith='b')
    #data = Product.objects.filter(tags__isnull=True)

#filter date time
    #data = Review.objects.filter(created_at__year=2023)
    #data = Review.objects.filter(created_at__month=2023)


# filter 2 values
    #data = Product.objects.filter(price__gt=80,quantity__lt=10) # and
    # data = Product.objects.filter(
    #      Q(price__gt=80) |
    #      Q(quantity__lt=10)
    # )  #or

    # data = Product.objects.filter(
    #      Q(price__gt=80) &
    #      Q(quantity__lt=10)
    # ) and
 
    # data = Product.objects.filter(
    #      Q(price__gt=80) |
    #      ~Q(quantity__lt=10)  
    # )     # or with not

    #data = Product.objects.filter(price=F('quantity'))# compare between to colum
    #data = Product.objects.all().order_by('name') #الترتيب بالاسم
    #data = Product.objects.order_by('name')#ترتيب تصاعدي
    #data = Product.objects.order_by('-name')#ترتيب تنازلي
    #data = Product.objects.order_by('name').reverse()#تنازلي

    #data = Product.objects.order_by('name','quantity')#two colum
    #data = Product.objects.order_by('name','-quantity')

    #data = Product.objects.order_by('name')[0]#هذا المجموعه لاتعمل في الفرونتاند بسبب لانه يرجعوا عنصر واحد واحنا الان عاملين لوب ولو عملنا عنصر واحد راح تشتغل
    #data = Product.objects.order_by('name')[-1]
    #data = Product.objects.earliest('name')
    #data = Product.objects.latest('name')

     #slice
    #data = Product.objects.all()[:10] #اظهار اول عشره
    #data = Product.objects.all()[10:20]
     
      #select columns
    #data = Product.objects.values('name','price')
    #data = Product.objects.values('name','price','brand__name')
    #data = Product.objects.values_list('name','price','brand__name')

    #remove duplicate
    #data = Product.objects.all().distinct()

    #data = Product.objects.only('name','price')
    #data = Product.objects.defer('slug','description')#هنا يتم استبعاد الا في الاقواس

    #aggregation

    # data = Product.objects.aggregate(Sum('quantity'))
    #data=Product.objects.aggregate(Avg('price'))
   
    #annotate

    #data=Product.objects.annotate(price_with_tax= F('price')*1.2)



     return render(request,'product/debug.html',{'data':data})
    
 




class ProductList(ListView):
    model = Product
    paginate_by = 30



class ProductDetail(DetailView):
    model = Product    


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"]=Review.objects.filter(product=self.get_object())
        context["related_products"]=Product.objects.filter(brand = self.get_object().brand)
        return context
    
class BrandList(ListView):
    model = Brand  
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
    paginate_by = 20




class BrandDetail(ListView) :
   model = Product
   template_name ='product/brand_detail.html' 
   paginate_by = 20


   def get_queryset(self) :
      brand = Brand.objects.get(slug =self.kwargs['slug'])
      return super().get_queryset().filter(brand=brand)



   def get_context_data(self, **kwargs) :
      context=super().get_context_data(**kwargs)
      context["brand"]= Brand.objects.filter(slug =self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
      return context
    
def add_review(request,slug):
       product = Product.objects.get(slug = slug)
       

       rate = request.POST['rate']  #ممكن يكتب هذا الكود  rate = request.POST.get('rate)
       review = request.POST['review']

       Review.objects.create(
           product = product,
           rate = rate,
           review = review,
           user = request.user
       )
       reviews =Review.objects.filter(product=product)
       html = render_to_string('include/reviews_include.html',{'reviews':reviews})
       return JsonResponse({'result':html})


    #    return redirect(f'/products/{product.slug}')