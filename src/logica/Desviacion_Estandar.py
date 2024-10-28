from src.logica.Promedio import Promedio


class CalculoNoPosible(Exception):
    pass


class DesviacionEstandar:
    def __init__(self, datos):
        self.__datos = datos

    def calcular_desviacion(self):
        try:
            if not self.__datos:
                raise CalculoNoPosible("No se puede calcular la desviación estándar de una lista vacía")
            if not all(isinstance(valor, (int, float)) for valor in self.__datos):
                raise TypeError("Todos los elementos deben ser números")
            if len(self.__datos) == 1:
                return 0
            if all(valor == 0 for valor in self.__datos):
                return "Cero"
            media = Promedio(self.__datos).calcular_media()
            suma_cuadratica = sum((valor - media) ** 2 for valor in self.__datos)
            return (suma_cuadratica / len(self.__datos)) ** 0.5
        except CalculoNoPosible:
            return None
        except TypeError:
            return "TypeError"
