from django.contrib import admin
from shop.models import Supplier, Payment, Product

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Payment)
admin.site.register(Product)


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields=('closing_balance')
