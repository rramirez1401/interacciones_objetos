## Defino la clase para crear el nuevo producto
class CrearProducto:
    def __init__(self, nombre:str, precio:int, stock:int = 0):
        self.__nombre_producto = nombre
        self.__precio_producto = precio
        self.stock_producto = stock

    ## GETTER DEL NOMBRE
    @property
    def nombre_producto(self):
        return self.__nombre_producto

    ## GETTER DEL PRECIO    
    @property
    def precio_producto(self):
        return self.__precio_producto

    ## MÉTODO PARA MOSTRAR LA INFO DEL PRODUCTO 
    def mostrar_objeto(self):
        return f"{self.nombre_producto:<{25}}{self.stock_producto:<{10}}{self.precio_producto:<{15}}"
    
    ## MÉTODO PARA MOSTRAR LA INFO DEL PRODUCTO SIN EL ATRIBUTO DE STOCK
    def mostrar_objeto_sin_stock(self):
        return f"{self.nombre_producto:<{25}}{self.precio_producto:<{15}}"
    

    ## SOBRECARGA DE MÉTODOS DUNDER PARA REALIZAR OPERACIONES CORRESPONDIENTES
    def __eq__(self, otro):
        if isinstance(otro, CrearProducto):
            return self.nombre_producto == otro.nombre_producto
        elif isinstance(otro, str):
            return self.nombre_producto == otro
        elif isinstance(otro, int):
            return self.stock_producto == otro
        return False

    def __add__(self, otro_producto):
        self.stock_producto += otro_producto.stock_producto
        return self
    
    def __le__(self, otro):
        return self.stock_producto <= otro
    
    def __ge__(self, otro):
        return self.precio_producto <= otro

    def __sub__(self, otro):
        self.stock_producto -= otro
        if self.stock_producto <= 0:
            self.stock_producto = 0
        return self