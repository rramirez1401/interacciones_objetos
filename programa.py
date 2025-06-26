from herramientas import Herramientas
import os
from tienda import *

############ DEFINO TODAS LAS FUNCIONES QUE NECESITO PARA EL PROGRAMA ############

## DEFINO LA FUNCION MENU_CREAR_TIENDA PARA EL MENÚ INICIAL QUE PREGUNTA QUE TIPO DE TIENDA SE QUIERE CREAR, EL NOMBRE Y EL COSTO DEL DELIVERY
def menu_crear_tienda():
    eleccion = ""
    while True:
        Herramientas.limpiar_pantalla()
        print("""
    Bienvenido!!!
    Que tipo de tienda quieres crear?
            
    1. Restaurant
    2. Supermercado
    3. Farmacia    
            
    Ingresa el número de tu elección
    """)
        eleccion = input("   >>> ")
        Herramientas.limpiar_pantalla()

        validar = Herramientas.validador(eleccion,["1", "2", "3"])
        
        if validar:
            break

    nombre_tienda = input("Ingresa el nombre de tu tienda\n\n    >>> ").capitalize()


    costo_delivery = 0
    while True:
        Herramientas.limpiar_pantalla()
        try:
            costo_delivery = int(input("Ingresa el costo del delivery\n\n    >>> "))
            break
        except ValueError:
            continue

    tipo_tienda = ""

    if eleccion == "1":
        mi_tienda = Restaurante(nombre_tienda, costo_delivery)
        tipo_tienda = "Restaurante"

    elif eleccion == "2":
        mi_tienda = Supermercado(nombre_tienda, costo_delivery)
        tipo_tienda = "Supermercado"

    else:
        mi_tienda = Farmacia(nombre_tienda, costo_delivery)
        tipo_tienda = "Farmacia"

    Herramientas.limpiar_pantalla()
    input("Ingresa los productos de tu tienda\n\nEnter para continuar")

    return mi_tienda, tipo_tienda


## DEFINO LA FUNCION PREGUNTAR_PRODUCTOS QUE SE ENCARGA DE PREGUNTAR AL USUARIO POR LOS PRODUCTOS A AGREGAR CON SU RESPECTIVO PRECIO Y STOCK
## CON UN CICLO WHILE PREGUNTO EL NOMBRE, PRECIO Y CANTIDAD QUE POSTERIORMENTE GENERA UNA LISTA Y LA ENVÍA AL METODO INGRESAR_PRODUCTRO DE LA TIENDA CREADA
def preguntar_productos(mi_tienda):
    while True:
        nuevo_producto = []
        Herramientas.limpiar_pantalla()
        prod_nombre = (input("Ingrese el producto o 'q' para para finalizar:\n\n    >>> ")).lower()
        if prod_nombre in ["q", "Q"]:
            break
        nuevo_producto.append(prod_nombre)

        Herramientas.limpiar_pantalla()
        try:
            prod_precio = int(input("Ingrese el precio del producto:\n\n    >>> "))
            nuevo_producto.append(prod_precio)
        except ValueError:
            input("Entrada no válida intenta ingresar nuevamente el producto\nEnter para continuar...")
            continue

        Herramientas.limpiar_pantalla()
        prod_cantidad = input("Ingrese la cantidad de productos a ingresar (opcional):\n\n    >>> ")
        if prod_cantidad != "":
            try:
                prod_cantidad = int(prod_cantidad)
                nuevo_producto.append(prod_cantidad)
            except ValueError:
                input("Entrada no válida intenta ingresar nuevamente el producto\nEnter para continuar...")
                continue
        mi_tienda.ingresar_producto(nuevo_producto)
    return mi_tienda



## DEFINO LA CLASE VENDER QUE PREGUNTA AL USUARIO QUE PRODUCTO QUIERE VENDER Y CUANTOS Y VERIFICA EL MATCH CON LA LISTA DE PRODUCTOS DE LA TIENDA
## SI SE HACE MATCH SE LLAMA A LA FUNCION REALIZAR_VENTA DE LA TIENDA CREADA Y SE ENVÍA EL INDEX DONDE SE ENCUENTRA EL PRODUCTO EN LA LISTA Y LA CANTIDAD SOLICITADA
def vender(mi_tienda, tipo_tienda):
    while True:
        try:
            Herramientas.limpiar_pantalla()
            prod_venta = (input("Qué producto deseas vender? presiona 'q' para para finalizar:\n\n    >>> ")).lower()
            if prod_venta in ["q", "Q"]:
                break
            cant_venta = int(input("Cuantos deseas vender?:\n\n    >>> "))

        except ValueError:
            continue

        if cant_venta > 3 and tipo_tienda == "Farmacia":
            input("Cantidad supera el límite ded 3 productos")
            break

        encontrado = False
        for i, prod in enumerate(mi_tienda.lista_productos):
            if prod.nombre_producto == prod_venta:
                encontrado = True
                mi_tienda.realizar_venta(i, cant_venta)
                print("aqui")

        if not encontrado:
            input("Producto no encontrado, intenta de nuevo por favor\nEnter para continuar...")
            continue

        break

## DEFINO LA FUNCION PARA EL MENU PRINCIPAL QUE REQUIERE COMO PARAMETRO LA INSTANCIA MI_TIENDA Y EL TIPO DE TIENDA
## AQUÍ SE DEFINE LO QUE SE QUIERE REALIZAR POSTERIOR A LA CREACION DE LA TIENDA Y LA AGREGACION INICIAL DE PRODUCTOS
def menu_principal(mi_tienda, tipo_tienda):
    while True:
        Herramientas.limpiar_pantalla()
        print("""
    Que deseas hacer a continuación?
            
    1. Agregar un nuevo producto
    2. Listar los productos existentes
    3. Realizar una venta
    4. Salir    
            
    Ingresa el número de tu elección
    """)
        eleccion = input("   >>> ")
        Herramientas.limpiar_pantalla()

        validar = Herramientas.validador(eleccion,["1", "2", "3", "4"])

        
        if validar:

            if eleccion == "1":
                preguntar_productos(mi_tienda)

            
            elif eleccion == "2":
                print(mi_tienda.listar_productos(tipo_tienda))
                input("\nEnter para continuar\n")

            elif eleccion == "3":
                vender(mi_tienda, tipo_tienda)

            elif eleccion == "4":
                input("VUELVE PRONTO!!!\nEnter para continuar...")
                exit()
        

## FINALMENTE DETERMINO EL ORDEN PARA LLAMAR A LAS FUNCIONES CREADAS
mi_tienda, tipo_tienda = menu_crear_tienda()
        
mi_tienda = preguntar_productos(mi_tienda)

menu_principal(mi_tienda, tipo_tienda)



