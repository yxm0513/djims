from django.contrib import admin

from djims.product.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)