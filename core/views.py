from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db import transaction
from .models import Producto, Carrito, CarritoItem, Orden, OrdenItem
from .forms import FormularioRegistro, FormularioProducto, FormularioCarrito


def inicio(request):
    productos_destacados = Producto.objects.all()[:4]
    return render(request, 'core/inicio.html', {
        'productos_destacados': productos_destacados,
        'titulo': 'Inicio',
    })


def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'core/catalogo.html', {
        'productos': productos,
        'titulo': 'Catálogo',
    })


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    formulario = FormularioCarrito(max_stock=producto.stock)
    return render(request, 'core/detalle_producto.html', {
        'producto': producto,
        'formulario': formulario,
        'titulo': producto.nombre,
    })


def registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cuenta creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('iniciar_sesion')
    else:
        formulario = FormularioRegistro()
    return render(request, 'core/registro.html', {
        'formulario': formulario,
        'titulo': 'Registro',
    })


@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'core/carrito.html', {
        'carrito': carrito,
        'titulo': 'Mi Carrito',
    })


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        formulario = FormularioCarrito(
            request.POST,
            max_stock=producto.stock
        )
        if formulario.is_valid():
            cantidad = formulario.cleaned_data['cantidad']
            if cantidad > producto.stock:
                messages.error(
                    request,
                    f'Stock insuficiente. Disponible: {producto.stock}'
                )
                return redirect('detalle_producto', producto_id=producto.id)

            item, creado = CarritoItem.objects.get_or_create(
                carrito=carrito,
                producto=producto,
                defaults={'cantidad': cantidad}
            )
            if not creado:
                nueva_cantidad = item.cantidad + cantidad
                if nueva_cantidad > producto.stock:
                    messages.error(
                        request,
                        f'Stock insuficiente. Ya tienes {item.cantidad} en tu carrito.'
                    )
                    return redirect('ver_carrito')
                item.cantidad = nueva_cantidad
                item.save()

            messages.success(
                request,
                f'"{producto.nombre}" añadido al carrito.'
            )
            return redirect('ver_carrito')

    return redirect('detalle_producto', producto_id=producto.id)


@login_required
def actualizar_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=request.user)

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        if cantidad < 1:
            messages.error(request, 'La cantidad debe ser al menos 1.')
        elif cantidad > item.producto.stock:
            messages.error(
                request,
                f'Stock insuficiente. Disponible: {item.producto.stock}'
            )
        else:
            item.cantidad = cantidad
            item.save()
            messages.success(request, 'Carrito actualizado.')

    return redirect('ver_carrito')


@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=request.user)
    producto_nombre = item.producto.nombre
    item.delete()
    messages.success(request, f'"{producto_nombre}" eliminado del carrito.')
    return redirect('ver_carrito')


@login_required
@transaction.atomic
def checkout(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if not carrito or not carrito.items.exists():
        messages.error(request, 'Tu carrito está vacío.')
        return redirect('catalogo')

    for item in carrito.items.all():
        if item.cantidad > item.producto.stock:
            messages.error(
                request,
                f'Stock insuficiente para "{item.producto.nombre}". '
                f'Disponible: {item.producto.stock}'
            )
            return redirect('ver_carrito')

    orden = Orden.objects.create(
        usuario=request.user,
        estado='confirmada'
    )

    for item in carrito.items.all():
        OrdenItem.objects.create(
            orden=orden,
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio
        )
        producto = item.producto
        producto.stock -= item.cantidad
        producto.save()

    carrito.items.all().delete()

    messages.success(request, '¡Compra realizada con éxito!')
    return redirect('detalle_orden', orden_id=orden.id)


@login_required
def detalle_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id, usuario=request.user)
    return render(request, 'core/detalle_orden.html', {
        'orden': orden,
        'titulo': f'Orden #{orden.id}',
    })


@login_required
def mis_ordenes(request):
    ordenes = Orden.objects.filter(usuario=request.user)
    return render(request, 'core/mis_ordenes.html', {
        'ordenes': ordenes,
        'titulo': 'Mis Órdenes',
    })


@staff_member_required
def panel_admin(request):
    total_productos = Producto.objects.count()
    total_ordenes = Orden.objects.count()
    productos_bajo_stock = Producto.objects.filter(stock__lt=5).count()
    ordenes_pendientes = Orden.objects.filter(estado='pendiente').count()
    return render(request, 'core/panel_admin.html', {
        'total_productos': total_productos,
        'total_ordenes': total_ordenes,
        'productos_bajo_stock': productos_bajo_stock,
        'ordenes_pendientes': ordenes_pendientes,
        'titulo': 'Panel de Administración',
    })


@staff_member_required
def gestionar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/gestionar_productos.html', {
        'productos': productos,
        'titulo': 'Gestionar Productos',
    })


@staff_member_required
def crear_producto(request):
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('gestionar_productos')
    else:
        formulario = FormularioProducto()
    return render(request, 'core/producto_form.html', {
        'formulario': formulario,
        'titulo': 'Crear Producto',
        'accion': 'Crear',
    })


@staff_member_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('gestionar_productos')
    else:
        formulario = FormularioProducto(instance=producto)
    return render(request, 'core/producto_form.html', {
        'formulario': formulario,
        'titulo': 'Editar Producto',
        'accion': 'Guardar Cambios',
        'producto': producto,
    })


@staff_member_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('gestionar_productos')
    return render(request, 'core/confirmar_eliminar.html', {
        'producto': producto,
        'titulo': 'Eliminar Producto',
    })


@staff_member_required
def ordenes_admin(request):
    ordenes = Orden.objects.all()
    return render(request, 'core/ordenes_admin.html', {
        'ordenes': ordenes,
        'titulo': 'Órdenes',
    })
