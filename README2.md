# MercadoM8 - E-Commerce MVP

Plataforma de comercio electronico construida con Django + SQLite3. MVP funcional con catalogo, carrito de compras, autenticacion y panel de administracion.

---
## Enlace al repositorio público

https://github.com/EnriqueMora-GH/m8-final

## Requisitos

- **Python** 3.10, 3.11 o 3.12
- **Git** (para clonar el repositorio)
- **Pip** (viene con Python)

No necesitas instalar PostgreSQL, MySQL, Node.js ni ninguna otra herramienta.

---

## Instalacion

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd m8-final
```

### 2. Crear y activar entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Veras `(venv)` al inicio de la linea cuando este activo.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Esto instala:
- **Django** — framework web
- **Gunicorn** — servidor web para produccion
- **WhiteNoise** — sirve archivos estaticos en produccion

---

## Ejecucion en local

### Migraciones (si empiezas desde cero)

```bash
python manage.py migrate
```

### Poblar base de datos con datos de ejemplo

```bash
python seed.py
```

Esto crea 12 productos tecnologicos y el usuario administrador.

### Iniciar servidor de desarrollo

```bash
python manage.py runserver
```

Abre **http://127.0.0.1:8000/** en tu navegador.

---

## Credenciales de prueba

### Administrador (acceso total al panel)

| Campo | Valor |
|-------|-------|
| Usuario | `admin` |
| Contrasena | `admin123` |

### Cliente (usuario regular registrado)

| Campo | Valor |
|-------|-------|
| Usuario | `cliente` |
| Contrasena | `cliente123` |

> El cliente debe crearse manualmente desde `/registro/` o puedes registrarte con tus propios datos.

---

## Rutas principales

### Publicas (sin autenticacion)

| Ruta | Descripcion |
|------|-------------|
| `/` | Pagina de inicio con productos destacados |
| `/catalogo/` | Catalogo completo de productos |
| `/producto/<id>/` | Detalle de un producto |
| `/registro/` | Crear cuenta de usuario |
| `/iniciar-sesion/` | Iniciar sesion |

### Cliente (requiere autenticacion)

| Ruta | Descripcion |
|------|-------------|
| `/carrito/` | Ver y gestionar carrito de compras |
| `/carrito/agregar/<id>/` | Agregar producto al carrito |
| `/checkout/` | Confirmar compra |
| `/mis-ordenes/` | Historial de ordenes |
| `/orden/<id>/` | Detalle de una orden |

### Administrador (requiere staff/superuser)

| Ruta | Descripcion |
|------|-------------|
| `/admin/` | Panel de administracion de Django |
| `/panel-admin/` | Dashboard personalizado |
| `/panel-admin/productos/` | CRUD de productos |
| `/panel-admin/productos/crear/` | Crear nuevo producto |
| `/panel-admin/productos/editar/<id>/` | Editar producto |
| `/panel-admin/productos/eliminar/<id>/` | Eliminar producto |
| `/panel-admin/ordenes/` | Ver todas las ordenes |

---

## Capturas de pantalla

### Pagina de inicio / Catalogo

![Home y catalogo](docs/screenshots/home-catalogo.png)

*Vista del catalogo de productos con tarjetas que muestran imagen, nombre, descripcion y precio en pesos chilenos.*

### Carrito de compras

![Carrito](doc/screenshots/carrito.png)

*Carrito con productos agregados, cantidades editables y total calculado automaticamente.*

### Panel de administracion

![Admin panel](doc/screenshots/admin-panel.png)

*Dashboard de administracion con resumen de productos, ordenes, stock bajo y acceso a gestion.*

> Las capturas de pantalla deben agregarse en `doc/screenshots/`. Toma captures de tu aplicacion corriendo en local y guardalas con esos nombres.

---

## Estructura del proyecto

```
m8-final/
├── ecommerce/              # Configuracion del proyecto Django
│   ├── settings.py         # BD, apps, seguridad, estaticos
│   ├── urls.py             # Rutas principales
│   └── wsgi.py             # Entry point para Gunicorn
├── core/                   # Aplicacion principal
│   ├── models.py           # Producto, Carrito, CarritoItem, Orden, OrdenItem
│   ├── views.py            # Logica de cada pagina
│   ├── forms.py            # Formularios (registro, login, productos, carrito)
│   ├── urls.py             # Rutas de la aplicacion
│   ├── admin.py            # Configuracion del panel admin de Django
│   ├── context_processors.py  # Contador global del carrito
│   ├── templates/          # Plantillas HTML
│   └── static/             # CSS personalizado
├── doc/
│   └── INSTALACION.md      # Guia detallada para principiantes
├── seed.py                 # Script para poblar la BD
├── build.sh                # Script de deploy para Render
├── requirements.txt        # Dependencias del proyecto
├── db.sqlite3              # Base de datos (incluida en git)
└── manage.py               # Control remoto de Django
```

---

## Paleta de colores

| Color | Hex | Uso |
|-------|-----|-----|
| Azul | `#6c9fe7` | Navbar, botones primarios, encabezados de tabla |
| Azul oscuro | `#476187` | Hover, botones secundarios |
| Casi negro | `#262322` | Footer, texto principal |
| Cafe | `#895438` | Precios, acentos |
| Naranja | `#e6844e` | Botones de peligro/eliminar |

---

## Tecnologias

- **Backend:** Django 6.0+ (Python)
- **Base de datos:** SQLite3
- **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Servidor:** Gunicorn + WhiteNoise
- **Hosting:** Render (Web Service)
