class CalculoNoPosible(Exception):
    pass


class Promedio:
    def __init__(self, datos):
        self.__datos = datos

    def calcular_media(self):
        try:
            if not self.__datos:
                raise CalculoNoPosible("No se puede calcular el promedio de una lista vacía")
            if not all(isinstance(valor, (int, float)) for valor in self.__datos):
                raise TypeError("Todos los elementos deben ser números")
            if all(valor == 0 for valor in self.__datos):
                return "Cero"
            return sum(self.__datos) / len(self.__datos)
        except CalculoNoPosible:
            return None
        except TypeError:
            return "TypeError"
