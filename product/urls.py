from django.urls import path
from .views import ProductList , ProductDetail,BrandList ,BrandDetail,queryst_debug

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',queryst_debug),
    path('<slug:slug>',ProductDetail.as_view()),
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),

]
