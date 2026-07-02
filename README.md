# MercadoM8 - E-Commerce MVP

Una plataforma de comercio electrónico funcional (MVP) construida con Django y SQLite3, diseñada como proyecto final de portafolio.

## Stack Tecnológico

- **Backend:** Django 6.0+ (Python)
- **Base de Datos:** SQLite3
- **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Servidor:** Gunicorn + WhiteNoise (archivos estáticos)

## Funcionalidades

- Catálogo de productos con 12 productos de tecnología
- Carrito de compras con actualización dinámica
- Sistema de autenticación (registro/inicio de sesión)
- Flujo completo de compra (checkout)
- Panel de administración para CRUD de productos
- Visualización de órdenes generadas
- Diseño responsivo con paleta de colores personalizada

## Roles

| Rol | Acceso |
| --- | ------ |
| **Cliente** | Navegar catálogo, gestionar carrito, realizar compras |
| **Administrador** | CRUD de productos, gestión de inventario, ver órdenes |

## Instalación Local

```bash
# Clonar el repositorio
git clone <repo-url>
cd m8-final

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos y poblar con datos semilla
python manage.py migrate
python seed.py

# Iniciar servidor
python manage.py runserver
```

El superusuario `admin` con contraseña `admin123` está preconfigurado.

## Despliegue en Render

Este proyecto usa SQLite3 como base de datos única, lo que simplifica el despliegue.

1. Fork/push este repositorio a GitHub (incluyendo `db.sqlite3`)
2. En Render, crea un **Web Service** conectado al repositorio
3. Configura:
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn ecommerce.wsgi:application`
4. Añade variables de entorno:
   - `SECRET_KEY`: Una clave secreta segura
   - `PYTHON_VERSION`: `3.12.1`
5. Desplegar

> ⚠️ Nota: Al usar SQLite3, los datos se pierden al redeployar. Es adecuado para fines demostrativos y de portafolio. Para producción real, se recomienda migrar a PostgreSQL.

## Enlace

[Ver aplicación en Render](#) (pendiente de despliegue)
