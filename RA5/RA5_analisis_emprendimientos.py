"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes  

def calcular_total(ventas):
    """Recibe una lista y retorna el total de ventas."""
    return sum(ventas)

def calcular_total(ventas):
    """Recibe una lista y retorna el total de ventas."""
    return sum(ventas)
def calcular_porcentaje_de_logro(total, meta):
    """Recibe el total de ventas y la meta, retorna el porcentaje de logro."""
    porcentaje = (total / meta) * 100
    return porcentaje
def calcular_clasificacion(porcentaje):
    """Recibe el porcentaje de logro y retorna la clasificación."""
    if porcentaje >= 100:
        mensaje = "meta superada, felicitaciones!!"
    elif porcentaje >= 90:
        mensaje = "ADVERTENCIA: meta no lograda."
    elif porcentaje >= 70:
        mensaje = "meta no alcanzada, revisar perdidas"
    return mensaje

def imprimir_reporte(datos_reporte):
    """imprime el reporte final de ventas por emprendimiento."""
 #encabezado
    print("\nREPORTE FINAL")
    print("-" * 60)      
    #print("la variable sedes es tipo:", type(sedes).__name__)
    for fila in datos_reporte:
        print(f"sede: {fila["nombre"]}")
        print(f"provincia: {fila["provincia"]}")
        print(f"tipo: {fila["tipo"]}")

        print(f"total ventas semanal: ₡{fila["total"]:,.2f}")
        print(f"cumplimiento de meta: {fila["porcentaje"]:,.2f}%")
        print(f"promedio diario: ₡{fila["total"]/5:,.2f}")
        print(fila["clasificacion"])
        #COMPLETAR LO QUE FALTA clasificacion,porcentaje meta,promedio semanal,
        print("-" * 60)

reporte = []
for emprendimiento in sedes:
    print("emprendimiento:", emprendimiento)
    print("tipo:", type(emprendimiento))
    print("Nombre:" , emprendimiento["nombre"])
    print("provincia:", emprendimiento["provincia"])
    print("ventas:", emprendimiento["ventas"])
    print("meta:", emprendimiento["meta"])
 #primer_emprendimiento = sedes[0]


    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]

    total_ventas = calcular_total(ventas)
    porcentaje_emprendimiento = calcular_porcentaje_de_logro(total_ventas, meta)
    clasificacion = calcular_clasificacion(porcentaje_emprendimiento)

    reporte.append({
        "nombre": emprendimiento["nombre"],
        "provincia": emprendimiento["provincia"],
        "tipo": emprendimiento["tipo"],
        "total": total_ventas, 
        "porcentaje": porcentaje_emprendimiento,
        "clasificacion": clasificacion
    })

imprimir_reporte(reporte)   