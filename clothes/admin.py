from django.contrib import admin
from .models import Product, ApparelSize, ProductCategories, Categories, Colors

# Register your models here.
admin.site.register(Product)
admin.site.register(ApparelSize)
admin.site.register(ProductCategories)
admin.site.register(Categories)
admin.site.register(Colors)