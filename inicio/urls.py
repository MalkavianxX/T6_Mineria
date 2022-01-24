from unicodedata import name
from django.urls import path
from . import views
 
urlpatterns = [
 
    path('',views.home,name="home"),
    path('agregar/',views.agregar,name="agregar"),
    path('guardar/',views.guardar,name="guardar"),
    path('eliminar/',views.eliminar,name="eliminar"),
    path('busqueda/',views.busqueda,name="busqueda"),
    path('borrarProducto/<str:id>/',views.borrarProducto,name="borrarProducto"),
    path('editar/',views.editar,name="editar"),
    path('guardarEditar/<str:id>/',views.guardarEditar,name="guardarEditar"),
    path('busquedaEditar/',views.busquedaEditar,name="busquedaEditar"),
    path('datos/',views.datos,name="datos"),
    path('generarDatos/',views.generarDatos,name="generarDatos"),
    path('contar_periodos/',views.contar_periodos,name="contar_periodos"),


] 

 