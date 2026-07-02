from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del producto")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        validators=[MinValueValidator(Decimal('1'))],
        verbose_name="Precio ($CLP)",
        help_text="Precio en pesos chilenos"
    )
    stock = models.PositiveIntegerField(verbose_name="Stock disponible")
    imagen = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="URL de la imagen"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def precio_formateado(self):
        return f"${self.precio:,.0f}".replace(",", ".")


class Carrito(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='carrito',
        verbose_name="Usuario"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())

    def total_formateado(self):
        return f"${self.total:,.0f}".replace(",", ".")


class CarritoItem(models.Model):
    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Carrito"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        verbose_name="Producto"
    )
    cantidad = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Cantidad"
    )

    class Meta:
        verbose_name = "Item del carrito"
        verbose_name_plural = "Items del carrito"
        unique_together = ('carrito', 'producto')

    def __str__(self):
        return f"{self.cantidad} × {self.producto.nombre}"

    @property
    def subtotal(self):
        return self.producto.precio * self.cantidad

    def subtotal_formateado(self):
        return f"${self.subtotal:,.0f}".replace(",", ".")


class Orden(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('enviada', 'Enviada'),
        ('entregada', 'Entregada'),
        ('cancelada', 'Cancelada'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ordenes',
        verbose_name="Usuario"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente',
        verbose_name="Estado"
    )

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Orden #{self.id} - {self.usuario.username}"

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())

    def total_formateado(self):
        return f"${self.total:,.0f}".replace(",", ".")


class OrdenItem(models.Model):
    orden = models.ForeignKey(
        Orden,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Orden"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        verbose_name="Producto"
    )
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name="Precio unitario ($CLP)"
    )

    class Meta:
        verbose_name = "Item de orden"
        verbose_name_plural = "Items de orden"

    def __str__(self):
        return f"{self.cantidad} × {self.producto.nombre}"

    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad

    def subtotal_formateado(self):
        return f"${self.subtotal:,.0f}".replace(",", ".")
