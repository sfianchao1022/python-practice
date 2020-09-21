from django.contrib import admin
from products.models import Products, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# Register your models here.
admin.site.register(Products, ProductsAdmin)
admin.site.register(Offer, OfferAdmin)