from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
import datetime
from product.models import Product
from django.utils import timezone


# Create your models here.
CART_STATUS = (
       ('InProgress','InProgress'),
       ('Completed' , 'Completed'),
   )



class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=10,choices=CART_STATUS)


    def __str__(self):
        return str(self.user)
    

    def cart_total(self):
        total = 0
        for item in self.cart_detail.all():
            total += item.total
        return total    



class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField()
    total = models.FloatField(null=True,blank=True)


    def __str__(self):
        return str(self.cart)



ORDER_STATUS= (
    ("Recived","Recived"),
    ("Processed","Processed"),
    ("Shipped","Shipped"),
    ("Delivered","Delivered"),
)


class Order(models.Model):
    
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=10,choices=ORDER_STATUS)
    code = models.CharField(max_length=10,default=generate_code())
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    coupon = models.ForeignKey('Coupon',related_name='order_coupon',on_delete=models.SET_NULL,null=True,blank=True)
    total_after_coupon = models.FloatField(null=True,blank=True)



    
    def __str__(self):
        return str(self.user)





class OrderDetail(models.Model):
    order = models.ForeignKey(Cart,related_name='order_detail',on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField(null=True,blank=True)


   
    def __str__(self):
        return str(self.order)




class Coupon(models.Model):
    code = models.CharField(max_length=20)
    discount = models.IntegerField()
    quantity = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True,blank=True)


    def __str__(self):
        return self.code
    

    def save(self,*args,**kwargs) :
        week = datetime.timedelta(days=7)
        self.end_date = self.start_date + week
        return super(Coupon,self).save(*args,**kwargs)