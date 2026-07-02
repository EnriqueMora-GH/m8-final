from .models import Carrito


def carrito_contador(request):
    contador = 0
    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
        if carrito:
            contador = sum(item.cantidad for item in carrito.items.all())
    return {'carrito_contador': contador}
