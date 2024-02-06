from django.urls import path
from .views import ProductList , ProductDetail,BrandList ,BrandDetail,queryst_debug,add_review
from .api import ProductListAPI,ProductDetailAPI,BrandListAPI,BrandDetailAPI

app_name ='product'

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',queryst_debug),
    path('<slug:slug>',ProductDetail.as_view()),
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),
    path('<slug:slug>/add-review',add_review,name='add-review'),

#api 
    path('api/list',ProductListAPI.as_view()),
    path('api/list/<int:pk>',ProductDetailAPI.as_view()),

    
    path('brands/api/list',BrandListAPI.as_view()),
    path('brands/api/list/<int:pk>',BrandDetailAPI.as_view()),

]
