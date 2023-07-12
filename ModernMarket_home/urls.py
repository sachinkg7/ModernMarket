
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/', views.logout, name='logout'),
    path('productpage/', views.productpage, name='productpage'),
    path('productpage/<int:pk>/', views.productdetails, name='productdetails'),
    path('cart/', views.cart, name='cart'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('addtowishlist/', views.addtowishlist, name='addtowishlist'),
    path('orderlist/', views.orderlist, name='orderlist'),
    path('checkout/', views.checkout, name='checkout'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('modifyrating/', views.modifyrating, name='modifyrating'),
    path('orderlist/<int:pk>/', views.orderdetails, name='orderdetails'),
    path('myprofile/', views.myprofile, name='myprofile'),
]
