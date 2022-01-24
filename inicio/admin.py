import site
from django.contrib import admin
from .models import Producto,Venta

class VentaAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)



class ProductoAdmin(admin.ModelAdmin) :

    readonly_fields = ("created",)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)

# Register your models here.
