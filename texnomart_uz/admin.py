from django.contrib import admin

from texnomart_uz.models import Category, Product, Image, Key, Value, Attribute

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Key)
admin.site.register(Value)
admin.site.register(Attribute)