from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'store'
urlpatterns = [
    url(r'^$', views.shop, name='menu'),
    path('product/<int:id>/', views.product, name='product'),
    path('category/<id>/', views.category, name='category'),
    path('cart/', views.cart, name='cart'),
    path('WishItems/', views.WishList, name='WishItems'),
    path('shipping/', views.shipping, name="shipping"),

    path('update_item/', views.updateItem, name="update_item"),
    path('add_to_wish_list/', views.addToWishList, name="addToWishList"),

    path('checkout/', views.checkout, name='checkout'),
    path('charge/', views.charge, name="charge"),
    path('success/<int:args>/', views.successMsg, name="success"),
    path('PaymentCompleted/', views.PaymentCompleted, name='PaymentCompleted')
]
