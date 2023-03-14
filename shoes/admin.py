from django.contrib import admin

# Register your models here.
from .models import Checkout
from .models import Adminshoe
# Register your models here.
class ShoeAdmin(admin.ModelAdmin):
    list_display = ('shoesname', 'shoesimage', 'shoesprice')

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('transactionID', 'amount', 'phone')

admin.site.register(Adminshoe, ShoeAdmin)
admin.site.register(Checkout, CheckoutAdmin)
