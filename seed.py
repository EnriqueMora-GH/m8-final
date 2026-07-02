import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from django.contrib.auth.models import User
from core.models import Producto


def crear_productos():
    productos_data = [
        {
            'nombre': 'Notebook Gamer Pro',
            'descripcion': 'Notebook de alto rendimiento con procesador Intel Core i7, 16GB RAM, '
                           'RTX 4060 y pantalla 15.6" Full HD. Ideal para gaming y trabajo pesado.',
            'precio': 799990,
            'stock': 15,
            'imagen': 'https://picsum.photos/seed/notebook/400/300',
        },
        {
            'nombre': 'Smartphone Galaxy X10',
            'descripcion': 'Smartphone con pantalla AMOLED 6.5", 128GB almacenamiento, '
                           'cámara triple 48MP + 8MP + 5MP y batería 5000mAh.',
            'precio': 249990,
            'stock': 30,
            'imagen': 'https://picsum.photos/seed/smartphone/400/300',
        },
        {
            'nombre': 'Audífonos Bluetooth Inalámbricos',
            'descripcion': 'Audífonos over-ear con cancelación de ruido activa, '
                           '30 horas de batería y sonido HD con graves profundos.',
            'precio': 45990,
            'stock': 50,
            'imagen': 'https://picsum.photos/seed/audifonos/400/300',
        },
        {
            'nombre': 'Teclado Mecánico RGB',
            'descripcion': 'Teclado mecánico gaming con switches Cherry MX Red, '
                           'retroiluminación RGB personalizable y construcción en aluminio.',
            'precio': 68990,
            'stock': 25,
            'imagen': 'https://picsum.photos/seed/teclado/400/300',
        },
        {
            'nombre': 'Monitor 27" 4K UHD',
            'descripcion': 'Monitor IPS 27 pulgadas con resolución 4K, 144Hz, '
                           'HDR10, soporte VESA y altavoces integrados.',
            'precio': 329990,
            'stock': 10,
            'imagen': 'https://picsum.photos/seed/monitor/400/300',
        },
        {
            'nombre': 'Mouse Ergonómico Vertical',
            'descripcion': 'Mouse vertical inalámbrico con diseño ergonómico, '
                           '6 botones programables y sensor óptico de 4000 DPI.',
            'precio': 25990,
            'stock': 40,
            'imagen': 'https://picsum.photos/seed/mouse/400/300',
        },
        {
            'nombre': 'Cámara Web HD 1080p',
            'descripcion': 'Cámara web con resolución Full HD 1080p, micrófono '
                           'estéreo integrado, corrección de luz automática y clip universal.',
            'precio': 34990,
            'stock': 20,
            'imagen': 'https://picsum.photos/seed/camara/400/300',
        },
        {
            'nombre': 'Disco SSD 1TB NVMe',
            'descripcion': 'Unidad de estado sólido NVMe M.2 de 1TB con velocidades '
                           'de lectura de hasta 3500MB/s. Perfecto para acelerar tu PC.',
            'precio': 79990,
            'stock': 35,
            'imagen': 'https://picsum.photos/seed/ssd/400/300',
        },
        {
            'nombre': 'Tablet Digital 10"',
            'descripcion': 'Tablet con pantalla IPS 10 pulgadas, 64GB almacenamiento, '
                           '4GB RAM, WiFi 6 y batería de 12 horas de duración.',
            'precio': 159990,
            'stock': 18,
            'imagen': 'https://picsum.photos/seed/tablet/400/300',
        },
        {
            'nombre': 'Parlante Bluetooth Portátil',
            'descripcion': 'Parlante inalámbrico resistente al agua IPX7, sonido '
                           '360 grados, 20 horas de batería y conector para tarjeta SD.',
            'precio': 29990,
            'stock': 45,
            'imagen': 'https://picsum.photos/seed/parlante/400/300',
        },
        {
            'nombre': 'Cargador Rápido USB-C 65W',
            'descripcion': 'Cargador GaN compacto de 65W con puerto USB-C, '
                           'compatible con laptops, tablets y smartphones. Carga rápida Power Delivery.',
            'precio': 19990,
            'stock': 60,
            'imagen': 'https://picsum.photos/seed/cargador/400/300',
        },
        {
            'nombre': 'Hub USB-C Multipuerto',
            'descripcion': 'Hub USB-C con 7 puertos: 2x USB-A 3.0, HDMI 4K, '
                           'lector de tarjetas SD/microSD, Ethernet y PD 100W.',
            'precio': 24990,
            'stock': 30,
            'imagen': 'https://picsum.photos/seed/hub/400/300',
        },
    ]

    for data in productos_data:
        producto, creado = Producto.objects.get_or_create(
            nombre=data['nombre'],
            defaults=data
        )
        if creado:
            print(f"  Creado: {producto.nombre} - ${producto.precio:,}")
        else:
            print(f"  Ya existe: {producto.nombre}")

    print(f"\nTotal de productos: {Producto.objects.count()}")


def crear_superusuario():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@mercadom8.cl',
            password='admin123'
        )
        print("Superusuario 'admin' creado (contraseña: admin123)")
    else:
        print("Superusuario 'admin' ya existe")


if __name__ == '__main__':
    print("=== Poblando base de datos ===\n")
    crear_productos()
    print()
    crear_superusuario()
    print("\n¡Base de datos lista!")
