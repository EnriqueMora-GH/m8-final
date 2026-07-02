# Guia Completa de Instalacion - MercadoM8 E-Commerce MVP

Esta guia esta pensada para **principiantes absolutos**. Explica paso a paso que instalar, por que se hace cada cosa y como funciona cada pieza del proyecto.

---

## Indice

1. [Que es este proyecto?](#1-que-es-este-proyecto)
2. [Que necesito instalar?](#2-que-necesito-instalar)
3. [Paso a paso: instalar Python](#3-paso-a-paso-instalar-python)
4. [Paso a paso: clonar el proyecto](#4-paso-a-paso-clonar-el-proyecto)
5. [Paso a paso: entorno virtual](#5-paso-a-paso-entorno-virtual)
6. [Paso a paso: instalar dependencias](#6-paso-a-paso-instalar-dependencias)
7. [Paso a paso: preparar la base de datos](#7-paso-a-paso-preparar-la-base-de-datos)
8. [Paso a paso: poblar con datos de prueba](#8-paso-a-paso-poblar-con-datos-de-prueba)
9. [Paso a paso: ejecutar el servidor](#9-paso-a-paso-ejecutar-el-servidor)
10. [Que es cada carpeta y archivo?](#10-que-es-cada-carpeta-y-archivo)
11. [Decisiones tecnicas tomadas](#11-decisiones-tecnicas-tomadas)
12. [Solucion de problemas comunes](#12-solucion-de-problemas-comunes)

---

## 1. Que es este proyecto?

**MercadoM8** es una tienda online sencilla pero completa. Permite:

- Ver un catalogo de productos tecnologicos.
- Registrarse e iniciar sesion.
- Agregar productos a un carrito de compras.
- Modificar cantidades o eliminar productos del carrito.
- Confirmar la compra (esto crea una orden o pedido).
- Que un administrador gestione los productos (crear, editar, eliminar).

Esta construido con **Django** (un framework de Python para hacer paginas web) y usa **SQLite3** como base de datos (un archivo que se guarda en el mismo proyecto, sin necesidad de instalar un servidor de base de datos).

---

## 2. Que necesito instalar?

| Programa | Version | Para que sirve? |
|----------|---------|------------------|
| **Python** | 3.10, 3.11 o 3.12 | Lenguaje de programacion del proyecto |
| **Git** | Cualquiera reciente | Descargar el proyecto desde GitHub |

No necesitas instalar PostgreSQL, MySQL, Node.js ni nada mas.

---

## 3. Paso a paso: instalar Python

### Windows
1. Ve a [python.org/downloads](https://www.python.org/downloads/)
2. Descarga Python 3.12 (boton amarillo grande)
3. Ejecuta el instalador y marca **"Add Python to PATH"**
4. Haz clic en "Install Now"
5. Abre "Simbolo del sistema" (escribe `cmd` en el menu Inicio)
6. Verifica: `python --version` (debe mostrar `Python 3.12.x`)

### macOS
1. Abre Terminal (Spotlight > "Terminal")
2. Instala Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Instala Python: `brew install python@3.12`
4. Verifica: `python3 --version`

### Linux (Ubuntu/Debian)
1. Abre Terminal
2. `sudo apt update && sudo apt install python3 python3-pip python3-venv -y`
3. Verifica: `python3 --version`

---

## 4. Paso a paso: clonar el proyecto

"Clonar" = descargar el proyecto desde GitHub a tu PC.

1. Instala Git si no lo tienes:
   - Windows: [git-scm.com](https://git-scm.com/)
   - macOS: `brew install git`
   - Linux: `sudo apt install git -y`

2. Abre la Terminal y navega a donde quieras guardar el proyecto:
   ```bash
   cd Documentos
   ```

3. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   ```

4. Entra a la carpeta:
   ```bash
   cd m8-final
   ```

---

## 5. Paso a paso: entorno virtual

Un **entorno virtual** aísla las librerias de este proyecto para que no se mezclen con otros proyectos.

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

Cuando veas `(venv)` al inicio de la linea, el entorno esta activo.

> **Por que?** Sin entorno virtual, las librerias se instalan "globalmente" y pueden generarse conflictos entre proyectos.

---

## 6. Paso a paso: instalar dependencias

Con `(venv)` activo:
```bash
pip install -r requirements.txt
```

Esto instala:

| Libreria | Para que sirve |
|----------|----------------|
| **Django** | Framework web: maneja rutas, base de datos, formularios, autenticacion |
| **Gunicorn** | Servidor web para produccion (Render) |
| **WhiteNoise** | Sirve archivos CSS e imagenes en produccion |

---

## 7. Paso a paso: preparar la base de datos

El proyecto ya incluye `db.sqlite3` con datos. Si quieres regenerarla:
```bash
python manage.py migrate
```

Este comando crea las tablas en la base de datos segun los **modelos** definidos en `core/models.py`:

- **Producto**: nombre, descripcion, precio, stock, imagen
- **Carrito** y **CarritoItem**: cada usuario tiene un carrito con productos
- **Orden** y **OrdenItem**: cuando confirmas compra, se crea una orden. El precio se congela en ese momento.

---

## 8. Paso a paso: poblar con datos de prueba

"Poblar" = llenar la base de datos con ejemplos.
```bash
python seed.py
```

Este script:
1. **Crea 12 productos** tecnologicos con precios chilenos ($799.990, $249.990, etc.)
2. **Crea un superusuario** (admin):
   - Usuario: `admin`
   - Contrasena: `admin123`

Puedes ejecutarlo varias veces, no crea duplicados.

---

## 9. Paso a paso: ejecutar el servidor

Con `(venv)` activo:
```bash
python manage.py runserver
```

Abre tu navegador en **http://127.0.0.1:8000/**

### Rutas para probar:

| Ruta | Que ves |
|------|---------|
| `/` | Inicio con productos destacados |
| `/catalogo/` | Todos los productos |
| `/producto/1/` | Detalle del producto ID 1 |
| `/admin/` | Panel Django (admin / admin123) |
| `/iniciar-sesion/` | Login |
| `/registro/` | Registro de usuario nuevo |
| `/carrito/` | Carrito de compras |
| `/panel-admin/` | Panel personalizado para admins |

Presiona **Ctrl + C** para detener el servidor.

---

## 10. Que es cada carpeta y archivo?

### Raiz del proyecto

| Archivo | Que es |
|---------|--------|
| `manage.py` | Control remoto de Django (runserver, migrate, etc.) |
| `requirements.txt` | Lista de librerias externas |
| `db.sqlite3` | Base de datos completa en un solo archivo |
| `seed.py` | Script para llenar la BD con datos de ejemplo |
| `build.sh` | Script de construccion para Render |
| `.gitignore` | Archivos que Git debe ignorar |

### Carpeta `ecommerce/` (configuracion del proyecto)

| Archivo | Que es |
|---------|--------|
| `settings.py` | Configuracion general: BD, apps, seguridad, estaticos |
| `urls.py` | Mapa de rutas principales |
| `wsgi.py` | Punto de entrada para Gunicorn en produccion |

### Carpeta `core/` (la aplicacion)

| Archivo | Que es |
|---------|--------|
| `models.py` | Define las tablas de la BD (Producto, Carrito, Orden) |
| `views.py` | Logica de cada pagina (que datos mostrar y como procesarlos) |
| `forms.py` | Formularios (registro, login, productos, carrito) |
| `urls.py` | Rutas de la aplicacion (catalogo, carrito, admin, etc.) |
| `admin.py` | Configuracion del panel de administracion de Django |
| `context_processors.py` | Variable global del contador del carrito |
| `templates/core/` | Plantillas HTML de cada pagina |
| `templates/registration/` | Plantilla del login |
| `static/core/css/estilo.css` | Estilos personalizados con la paleta de colores |

### Carpeta `doc/`

| Archivo | Que es |
|---------|--------|
| `INSTALACION.md` | Este archivo que estas leyendo |

---

## 11. Decisiones tecnicas tomadas

### Por que SQLite3 y no PostgreSQL?

**Decision:** Usamos SQLite3 en lugar de PostgreSQL.

**Motivo:** Para un MVP de portafolio, SQLite3 simplifica enormemente el despliegue. No necesitas crear ni configurar un servicio de base de datos aparte en Render. Todo vive en un archivo (`db.sqlite3`) que viaja con el codigo. Esto es ideal para demostraciones, pero no recomendado para produccion real con multiples usuarios concurrentes.

### Por que incluimos `db.sqlite3` en el repositorio?

**Decision:** El archivo `db.sqlite3` se incluye en Git (lo quitamos del `.gitignore`).

**Motivo:** Render reconstruye el contenedor desde cero cada vez que haces deploy. Si la BD no esta en el repo, perderias los datos. Al incluirla, los productos y el usuario admin estan disponibles desde el primer deploy.

### Por que Django y no Flask o FastAPI?

**Decision:** Django.

**Motivo:** Django incluye "baterias incluidas": trae ORM, autenticacion, panel admin, formularios, mensajes y mas sin necesidad de librerias adicionales. Para un MVP con roles, carrito y panel admin, Django reduce drasticamente la cantidad de codigo necesario.

### Por que Bootstrap y CSS propio?

**Decision:** Bootstrap 5 para la maquetacion base + CSS personalizado con la paleta de colores.

**Motivo:** Bootstrap da una base responsiva y probada en minutos. El CSS personalizado aplica la paleta de colores (azul, azul oscuro, casi negro, cafe, naranja) definida en el PRD para darle identidad visual al proyecto.

### Por que Gunicorn + WhiteNoise?

**Decision:** Gunicorn como servidor WSGI y WhiteNoise para archivos estaticos.

**Motivo:** Django en desarrollo usa su propio servidor liviano, pero no es seguro ni eficiente para produccion. Gunicorn es el estandar para servir Django. WhiteNoise resuelve el problema de que Django no sirve archivos estaticos en produccion.

### Por que variables en espanol?

**Decision:** Todos los nombres de modelos, campos, formularios, URLs y templates estan en espanol.

**Motivo:** El publico objetivo del portafolio puede ser reclutadores hispanohablantes. Tener el codigo en espanol facilita la lectura y demuestra que el desarrollador puede trabajar con vocabulario tecnico en su idioma nativo.

### Por que precios sin decimales?

**Decision:** Los precios se almacenan como `DecimalField` con `decimal_places=0`.

**Motivo:** En Chile los precios se expresan en pesos sin decimales (ej: $799.990). Usar `decimal_places=0` simplifica la visualizacion y evita confusiones con centavos.

### Por que el carrito se guarda en la BD y no en sesion?

**Decision:** Usamos modelos `Carrito` y `CarritoItem` en la base de datos (no en la sesion del navegador).

**Motivo:** Persistencia: el carrito no se pierde si el usuario cierra el navegador. Ademas, es mas facil de implementar con Django ORM y permite consultas mas complejas.

### Por que el precio se congela al comprar?

**Decision:** `OrdenItem.precio_unitario` guarda el precio en el momento de la compra, separado del `Producto.precio` actual.

**Motivo:** Si el admin cambia el precio despues, la orden historica debe reflejar lo que el cliente realmente pago.

---

## 12. Solucion de problemas comunes

### Error: "python no se reconoce como un comando"

En Windows, significa que Python no esta en el PATH. Reinstala Python y marca "Add Python to PATH". Cierra y vuelve a abrir la terminal.

### Error: "pip no se reconoce como un comando"

Similar al anterior. Asegurate de tener Python instalado correctamente.

### Error: "No module named django"

```bash
pip install -r requirements.txt
```
Asegurate de tener el entorno virtual activo (`(venv)` visible).

### Error: "django.db.utils.OperationalError: no such table"

```bash
python manage.py migrate
```

### Error: el servidor no se ve en el navegador

Asegurate de que el servidor este corriendo (debe decir "Starting development server at http://127.0.0.1:8000/"). Luego escribe exactamente `http://127.0.0.1:8000/` en la barra de direcciones del navegador.

### Error al hacer deploy en Render

1. Verifica que `build.sh` tenga permisos de ejecucion: `chmod +x build.sh`
2. Revisa que `requirements.txt` este actualizado
3. Asegurate de que `db.sqlite3` este incluido en el repositorio
4. Revisa los logs de Render para mas detalles

### Error: puerto 8000 ya esta en uso

```bash
# Encuentra el proceso
lsof -i :8000
# Matelo (reemplaza PID con el numero)
kill -9 PID
```

O usa otro puerto:
```bash
python manage.py runserver 8080
```
