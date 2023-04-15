from django.contrib import admin
from.models import*

class ProductAdmin(admin.ModelAdmin):
    list_display = ("label", "price", "stock")

class CommandAdmin(admin.ModelAdmin):
    list_display = ("commandNumber", "name", "quality", "date_cmd")

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Command, CommandAdmin)
admin.site.register(CommandDetails)
admin.site.register(DeliveryInformation)

