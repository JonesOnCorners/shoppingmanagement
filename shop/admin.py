from django.contrib import admin
from shop.models import Supplier, Payment, Product

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Payment)
admin.site.register(Product)
