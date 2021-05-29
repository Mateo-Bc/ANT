from django.contrib import admin
from .models import *

# Register your models here.

class Categoria_Admin(admin.ModelAdmin):
    list_display = ['nombre',]

class Producto_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    list_display_links = ['nombre']

class Stock_Admin(admin.ModelAdmin):
    list_display = ['producto', 'cantidad']

class Venta_Admin(admin.ModelAdmin):
    list_display = ['articulo', 'unidades', 'precio_total']

admin.site.register(Categoria, Categoria_Admin)
admin.site.register(Proveedor, )
admin.site.register(Producto, Producto_Admin)
admin.site.register(Carro, )
admin.site.register(Stock, Stock_Admin)
admin.site.register(Venta, Venta_Admin)