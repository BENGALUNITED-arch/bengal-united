from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    
    # News Section
    path('news/<int:article_id>/', views.news_detail, name='news_detail'), 
    
    # Academy Programs
    path('programs/', views.programs_page, name='programs'),
    
    # Official Store
    path('shop/', views.shop_page, name='shop'),
    path('shop/product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    # Gallery
    path('gallery/', views.gallery_page, name='gallery'),
    
    # About Us (Inside Page)
    path('about/', views.about_detail, name='about_detail'),
]