from django.shortcuts import render
from .models import Producto,Venta
from random import randint,choice
import datetime
import time
from .funcionesPeriodos import contador_por_fechas as calcPeriodo
from .funcionesPeriodos import calcular_Porcentaje as porcentaje

def home(request):
    return render(request,"inicio/home.html")


def inicio(request):
    return render(request, "inicio/inicio.html")

def agregar(request):
    return render(request, "inicio/agregar.html")

def guardar(request):

    try:

        nuevo = Producto(
            id = request.GET.get("id"),
            nombre = request.GET.get("nombre"),
            precio = request.GET.get("precio"),
            stock = request.GET.get("stock")
        )
        nuevo.save()
    except:
        return render(request,"inicio/agregar.html",{"alert":1, "name":"alert-danger","mensaje":"Error el ID ya existe"})

    return render(request,"inicio/agregar.html",{"alert":1,"name":"alert-success","mensaje":"Hecho! Acción realizada con exito"})

def eliminar(request):
    
    return render(request,"inicio/eliminar.html") 

def busqueda(request):
    buscar = request.GET.get("busqueda")
    try:
    
        prod = Producto.objects.get(nombre = buscar)
        return render(request,"inicio/eliminar.html",{"obj":prod,"alert":2})     
    except:
        return render(request,"inicio/eliminar.html",{"alert":1, "name":"alert-warning","mensaje":"Error el producto no existe"})  

def borrarProducto(request,id):
    prod = Producto.objects.get(pk = id)
    prod.delete()
    return render(request,"inicio/eliminar.html",{"alert":1, "name":"alert-success","mensaje":"Producto eliminado"})     
    
def editar(request):
    return render(request,"inicio/editar.html")    

def busquedaEditar(request):
    buscar = request.GET.get("busqueda")
    try:
    
        prod = Producto.objects.get(nombre = buscar)
        return render(request,"inicio/editar.html",{"obj":prod,"alert":2})     
    except:
        return render(request,"inicio/editar.html",{"alert":1, "name":"alert-warning","mensaje":"Error el producto no existe"})  

def guardarEditar(request,id):  
    prod = Producto.objects.get(pk = id)
    prod.nombre = request.GET.get("nombre")
    prod.precio = request.GET.get("precio")
    prod.stock = request.GET.get("stock")
    prod.save()
    return render(request,"inicio/editar.html",{"alert":1, "name":"alert-success","mensaje":"Producto editado"})     

def datos(request):
    return render(request, "inicio/generar_datos.html")

def generarDatos(request):
    start = time.time()
    lista_id_producto = []
    obtener_productos = Producto.objects.all()

    for i in range(len(obtener_productos)):
        lista_id_producto.append(obtener_productos[i].id)

    dia = datetime.datetime.now()   
    for i in range(5000):
        verificar_venta = randint(1,10)
        if verificar_venta<6 and verificar_venta>0:
            siguiente_dia = dia + datetime.timedelta(days=i)
            dato = Venta(
                id = siguiente_dia ,
                numeroArticulo = Producto.objects.get(pk= str(choice(lista_id_producto))),
                descripcion =  str(choice("ABCDE")),
                cantidad = randint(10,50)
                )
            dato.save()
    end = time.time()
    tiempo_ejecucion =  end-start
    obtener_ventas = Venta.objects.all()
    numero_registros = len(obtener_ventas)
    efectividad = (100 * numero_registros)/5000

    return render(request, "inicio/mostrar_datos.html",{
        "num":str(numero_registros),
        "time":str(tiempo_ejecucion),
        "efect":str(efectividad)
        })


#VENTAS -- CONTADOR DE PERIODOS
def contar_periodos(request):

    obj = Venta.objects.all()
    total = len(obj)    
    for i in range(total):
        obj[i].id = obj[i].id.strftime('%m%d') # 10-12-2022 --> 1210
    contador_prim = contador_periodo_primavera(obj)
    contador_ver = contador_periodo_verano(obj)
    contador_oto = contador_periodo_otono(obj)
    contador_inv = total - (contador_prim+contador_oto+contador_ver)
    return render(request,"inicio/contador_periodo.html",{
        'prim':contador_prim,
        'ver':contador_ver,
        'oto':contador_oto,
        'inv':contador_inv,
        'primp':porcentaje(total,contador_prim),
        'verp':porcentaje(total,contador_ver),
        'otop':porcentaje(total,contador_oto),
        'invp':porcentaje(total,contador_inv),
        'ventas':total    
        })
def contador_periodo_otono(obj):
    fecha_inicial = datetime.date(2021,9,23)
    fecha_final = datetime.date(2022,12,22)

    return calcPeriodo(fecha_inicial,fecha_final,obj)


def contador_periodo_verano(obj):
    fecha_inicial = datetime.date(2021,6,23)
    fecha_final = datetime.date(2022,9,22)

    return calcPeriodo(fecha_inicial,fecha_final,obj)

def contador_periodo_primavera(obj):
    fecha_inicial = datetime.date(2021,3,21)
    fecha_final = datetime.date(2022,6,22)

    return calcPeriodo(fecha_inicial,fecha_final,obj)

























