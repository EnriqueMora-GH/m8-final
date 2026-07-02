from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import FormularioInicioSesion

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('registro/', views.registro, name='registro'),
    path(
        'iniciar-sesion/',
        auth_views.LoginView.as_view(
            template_name='registration/iniciar_sesion.html',
            authentication_form=FormularioInicioSesion,
        ),
        name='iniciar_sesion'
    ),
    path(
        'cerrar-sesion/',
        auth_views.LogoutView.as_view(next_page='inicio'),
        name='cerrar_sesion'
    ),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('orden/<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
    path('mis-ordenes/', views.mis_ordenes, name='mis_ordenes'),
    path('panel-admin/', views.panel_admin, name='panel_admin'),
    path('panel-admin/productos/', views.gestionar_productos, name='gestionar_productos'),
    path('panel-admin/productos/crear/', views.crear_producto, name='crear_producto'),
    path(
        'panel-admin/productos/editar/<int:producto_id>/',
        views.editar_producto,
        name='editar_producto'
    ),
    path(
        'panel-admin/productos/eliminar/<int:producto_id>/',
        views.eliminar_producto,
        name='eliminar_producto'
    ),
    path('panel-admin/ordenes/', views.ordenes_admin, name='ordenes_admin'),
]
