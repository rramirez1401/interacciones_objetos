from abc import ABC, abstractmethod
import os
from herramientas import Herramientas
from producto import CrearProducto

## DEFINO LA CLASE ABSTRACTA TIENDA
class Tienda(ABC):
    def __init__(self, nombre_tienda:str, costo_delivery:int):
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.lista_productos = []

    ## GETTER DEL NOMBRE DE LA TIENDA
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda

    ## GETTER DEL COSTO DEL DELIVERY
    @property
    def costo_delivery(self):
        return self.__costo_delivery

    ## DEFINO EL MÉTODO INGRESAR PRODUCTO QUE SIRVE PARA LAS TIENDAS QUE HEREDAN DE ESTA CLASE
    ## UTILIZO COMPOSICION FUERTE PARA LA VARIABLE PRODUCTO, LA CUAL ES UNA INSTANCIA DE CREAR_PRODUCTO
    def ingresar_producto(self, nuevo_producto:object):        
        producto = CrearProducto(*nuevo_producto)

        for i, prod in enumerate(self.lista_productos): 
            if prod.nombre_producto == producto:
                self.lista_productos[i] = prod + producto
                input("El producto ya existía se sumó la nueva cantidad\nEnter para continuar...")
                return

        self.lista_productos.append(producto)


    ## DEFINO EL MÉTODO ABSTRACTO LISTAR_PRODUCTOS QUE SE DEFINE DISTINTO EN CADA TIENDA
    @abstractmethod
    def listar_productos(self, tipo_tienda:str):
        pass
   
    
        
    ## DEFINO EL MÉTODO REALIZAR_VENTA QUE SIRVE PARA LAS TIENDAS QUE HEREDAN DE ESTA CLASE
    def realizar_venta(self, i, cant_venta:int):
        if self.lista_productos[i] == 0:
            input("No queda stock\nEnter para continuar...")
            return
        
        else:    
            self.lista_productos[i] - cant_venta
            input("Producto vendido\nEnter para continuar...")
            return

            
################################ CLASES QUE HEREDAN DE TIENDA ################################


##### CLASE RESTAURANTE #####
class Restaurante(Tienda):

    ## APLICO POLIMORFISMO PARA MODIFICAR EL COMPORTAMIENTO DE INGRESAR_PRODUCTO ADAPTADO A LOS REQUERIMIENTOS DE ESTA CLASE 
    def ingresar_producto(self, nuevo_producto:list):
            
            producto = CrearProducto(*nuevo_producto)

            for prod in self.lista_productos: 
                if prod == producto:
                    input("El producto ya existe, no se realiza ninguna modificación!!!\nEnter para continuar...")
                    return

            self.lista_productos.append(producto)

    ## APLICO POLIMORFISMO PARA MODIFICAR EL COMPORTAMIENTO DE LISTAR_PRODUCTOS ADAPTADO A LOS REQUERIMIENTOS DE ESTA CLASE
    ## ORGANIZO TODOS LO QUE SE REQUIERE IMPRIMIR DENTRO UNA VARIABLE LLAMADA A_RETORNAR PARA DEVOLVER UN F STRING CON TODA LA INFORMAACIÓN LISTA PARA IMPRIMIR
    def listar_productos(self, tipo_tienda:str):
        a_retornar = ""
        a_retornar += f"Listado de productos de {tipo_tienda} {self.nombre_tienda}\n"
        a_retornar += f"El costo de delivery es: {self.costo_delivery} pesos\n\n"
        a_retornar += f"{"PRODUCTO":{25}}{"PRECIO":{15}}{"PRECIO + DELIVERY":{15}}\n"
        for prod in self.lista_productos:
            a_retornar += f"{prod.mostrar_objeto_sin_stock()}{self.costo_delivery + prod.precio_producto}\n"

        return f"{a_retornar}"

    ## APLICO POLIMORFISMO PARA MODIFICAR EL COMPORTAMIENTO DE REALIZAR_VENTA ADAPTADO A LOS REQUERIMIENTOS DE ESTA CLASE
    def realizar_venta(self, i, cant_venta):
        input("Producto vendido\nEnter para continuar...")
        return

        

##### CLASE SUPERMERCADO #####
class Supermercado(Tienda):

    ## APLICO POLIMORFISMO PARA MODIFICAR EL COMPORTAMIENTO DE INGRESAR_PRODUCTO ADAPTADO A LOS REQUERIMIENTOS DE ESTA CLASE
    ## ORGANIZO TODOS LO QUE SE REQUIERE IMPRIMIR DENTRO UNA VARIABLE LLAMADA A_RETORNAR PARA DEVOLVER UN F STRING CON TODA LA INFORMAACIÓN LISTA PARA IMPRIMIR 
    def listar_productos(self, tipo_tienda:str):
        a_retornar = ""
        a_retornar += f"Listado de productos de {tipo_tienda} {self.nombre_tienda}\n"
        a_retornar += f"El costo de delivery es: {self.costo_delivery} pesos\n\n"
        a_retornar += f"{"PRODUCTO":{25}}{"STOCK":{10}}{"PRECIO":{15}}{"PRECIO + DELIVERY":{25}}{"OBSERVACION":{15}}\n"
        for prod in self.lista_productos:
            if prod.stock_producto <= 10:
                a_retornar += f"{(prod.mostrar_objeto())}{(self.costo_delivery + prod.precio_producto):<{25}}{"Pocos productos disponibles!!!"}\n"
            else:
                a_retornar += f"{(prod.mostrar_objeto())}{(self.costo_delivery + prod.precio_producto)}\n"

        return f"{a_retornar}"



##### CLASE FARMACIA #####
class Farmacia(Tienda):

    ## APLICO POLIMORFISMO PARA MODIFICAR EL COMPORTAMIENTO DE LISTAR_PRODUCTOS ADAPTADO A LOS REQUERIMIENTOS DE ESTA CLASE
    ## ORGANIZO TODOS LO QUE SE REQUIERE IMPRIMIR DENTRO UNA VARIABLE LLAMADA A_RETORNAR PARA DEVOLVER UN F STRING CON TODA LA INFORMAACIÓN LISTA PARA IMPRIMIR
    def listar_productos(self, tipo_tienda):
        a_retornar = ""
        a_retornar += f"Listado de productos de {tipo_tienda} {self.nombre_tienda}\n"
        a_retornar += f"El costo de delivery es: {self.costo_delivery} pesos\n\n"
        a_retornar += f"{"PRODUCTO":{25}}{"PRECIO":{15}}{"PRECIO + DELIVERY":{25}}{"OBSERVACION":{15}}\n"
        for prod in self.lista_productos:
            if prod.precio_producto >= 15000:
                a_retornar += f"{(prod.mostrar_objeto_sin_stock())}{(self.costo_delivery + prod.precio_producto):<{25}}{"Envío gratis al solicitar este producto!!!"}\n"
            else:
                a_retornar += f"{(prod.mostrar_objeto_sin_stock())}{(self.costo_delivery + prod.precio_producto)}\n"

        return f"{a_retornar}"


