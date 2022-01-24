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
    #obtener los registros que tiene la tabla ventas
    obj = Venta.objects.all()
    #obtener el tamaño de la tabla (5000 por ejemplo)
    total = len(obj)    
    #recorremos la tabla para modificar el formato de la fecha
    #por ejemplo la fecha en la tabla es 01-02-2022:12:09:12:3456... 
    #despues de este for la fecha saldria asi:
    # 0201
    for i in range(total):
        obj[i].id = obj[i].id.strftime('%m%d') # 10-12-2022 --> 1210
    #llamamos a las funciones para contar las ventas que hay en cada rango
    #las cuales retornan un entero, que es el numero de ventas que hay para ese rango
    contador_prim = contador_periodo_primavera(obj)
    contador_ver = contador_periodo_verano(obj)
    contador_oto = contador_periodo_otono(obj)
    #el contador invierno no tiene una funcion ya que las ventas que le corresponden
    #serian las que sobran de las demas
    contador_inv = total - (contador_prim+contador_oto+contador_ver)
    #esta parte llama a la template de html, la cual muestra los resultados
    return render(request,"inicio/contador_periodo.html",{
        'prim':contador_prim,
        'ver':contador_ver,
        'oto':contador_oto,
        'inv':contador_inv,
        #ESTA PARTE DE PORCENTAJE SOLO ES PARA SABER QUE TANTO POR CIENTO ES DEL TOTAL DE LAS VENTAS
        # POR EJEMPLO SI PRIM TIENE 600 VENTAS Y EL TOTAL DE VENTAS ES DE 5000
        #LA FUNCION PORCENTAJE DEVUELVE EN FORMA DE STRING EL % AL QUE CORRESPONDE 600 DE 5000
        
        'primp':porcentaje(total,contador_prim),
        'verp':porcentaje(total,contador_ver),
        'otop':porcentaje(total,contador_oto),
        'invp':porcentaje(total,contador_inv),
        'ventas':total    
        })
#aqui estan las funciones que cuentan, la cual tiene fecha que inicia el periodo
# y fecha con la que termina
# devuelve un entero, 
#la funcion calcPeriodo esta en el archivo "FUnciones Periodo.py sin embargo aqui lo muestro:"

#
#def contador_por_fechas(fecha_inicial,fecha_final, obj):
#       AQUI HACEMOS LO MISMO QUE EN LA FUNCION PRINCIPAL, CAMBIAMOS LA FECHA A UN ENTERO
        #LA CUAL ES MES Y DIA: 01/12/2022 A 1201
#    fecha_final = fecha_final.strftime('%m%d')
#    fecha_inicial = fecha_inicial.strftime('%m%d')    
#    f1 = int(fecha_inicial) #1012 tipo: Time --> 1012 tipo: Int
#    f2 = int(fecha_final)
#    contador = 0
#       RECORREMOS EL OBJETO QUE CONTIENE TODAS LAS VENTAS PARA ENCONTRAR LAS QUE
#          COINCIDEN CON EL RANGO
#    for i in range(len(obj)):   
#        if (int(obj[i].id) >= int(f1) and int(obj[i].id) <= int(f2)):
#            contador+=1 
#       SE DEVUELVE EL RESULTADO
#    return contador

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

























