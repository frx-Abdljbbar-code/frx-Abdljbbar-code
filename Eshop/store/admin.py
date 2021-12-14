from django.contrib import admin
from .models import ProductImage, Product, ShippingAddress, Order, OrderItem, WishItem, Categorys


class PostImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Product

@admin.register(ProductImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShippingAddress)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(WishItem)
admin.site.register(Categorys)
