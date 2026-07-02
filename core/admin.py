from django.contrib import admin
from .models import Producto, Carrito, CarritoItem, Orden, OrdenItem


@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'fecha_creacion']
    list_filter = ['fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['stock']


class OrdenItemInline(admin.TabularInline):
    model = OrdenItem
    readonly_fields = ['producto', 'cantidad', 'precio_unitario']
    extra = 0


@admin.register(Orden)
class AdminOrden(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'estado', 'fecha_creacion', 'total_formateado']
    list_filter = ['estado', 'fecha_creacion']
    search_fields = ['usuario__username']
    list_editable = ['estado']
    inlines = [OrdenItemInline]
    readonly_fields = ['usuario', 'fecha_creacion']


admin.site.register(Carrito)
admin.site.register(CarritoItem)
admin.site.register(OrdenItem)
