import datetime

def contador_por_fechas(fecha_inicial,fecha_final, obj):
    fecha_final = fecha_final.strftime('%m%d')
    fecha_inicial = fecha_inicial.strftime('%m%d')    
    f1 = int(fecha_inicial) #1012 tipo: Time --> 1012 tipo: Int
    f2 = int(fecha_final)
    contador = 0
    for i in range(len(obj)):   
        if (int(obj[i].id) >= int(f1) and int(obj[i].id) <= int(f2)):
            contador+=1 

    return contador

def calcular_Porcentaje(total,valor):
    porcentaje = (valor * 100)/total

    return "{0:.2f}".format(porcentaje)