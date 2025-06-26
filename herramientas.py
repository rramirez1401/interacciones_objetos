import os

### DEFINO LA CLASE HERRAMIENTAS PARA UTILIZARLAS EN CALQUIER MOMENTO SIN NECESIDAD DE INSTANCIAR
class Herramientas:
    @staticmethod
    def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def validador(texto_a_evaluar, lista_opciones):
        if texto_a_evaluar in lista_opciones:
            return True
        else:
            return False