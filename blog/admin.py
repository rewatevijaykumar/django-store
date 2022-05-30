from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Product

@register(Product)
class ProductAdmin(ModelAdmin):
    list_display=["name",]