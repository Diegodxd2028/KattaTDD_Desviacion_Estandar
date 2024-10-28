import unittest

from src.logica.Desviacion_Estandar import DesviacionEstandar
from src.logica.Promedio import Promedio


class PruebaOperaciones(unittest.TestCase):

    def test_promedio_lista_vacia(self):
        datos = Promedio([])
        self.assertIsNone(datos.calcular_media())

    def test_promedio_un_elemento(self):
        datos = Promedio([6])
        self.assertEqual(datos.calcular_media(), 6)

    def test_promedio_dos_elementos(self):
        datos = Promedio([2, 6])
        self.assertEqual(datos.calcular_media(), 4)

    def test_promedio_varios_elementos(self):
        datos = Promedio([4, 6, 8, 10, 12])
        self.assertEqual(datos.calcular_media(), (4 + 6 + 8 + 10 + 12) / 5)

    def test_promedio_todos_ceros(self):
        datos = Promedio([0, 0, 0, 0, 0])
        self.assertEqual(datos.calcular_media(), "Cero")

    def test_promedio_numeros_mixtos(self):
        datos = Promedio([-3, 8, 11, -1, -5])
        self.assertEqual(datos.calcular_media(), ((8 + 11) - (3 + 1 + 5)) / 5)

    def test_promedio_elementos_no_numericos(self):
        datos = Promedio(["a", "b", "c"])
        self.assertEqual(datos.calcular_media(), "TypeError")

    def test_desviacion_estandar_lista_vacia(self):
        datos = DesviacionEstandar([])
        self.assertIsNone(datos.calcular_desviacion())

    def test_desviacion_estandar_un_elemento(self):
        datos = DesviacionEstandar([8])
        self.assertEqual(datos.calcular_desviacion(), 0)

    def test_desviacion_estandar_dos_elementos(self):
        datos = DesviacionEstandar([4, 6])
        self.assertEqual(datos.calcular_desviacion(), 1)

    def test_desviacion_estandar_varios_elementos(self):
        datos = DesviacionEstandar([5, 6, 7])
        self.assertEqual(datos.calcular_desviacion(), (((5 - 6) ** 2 + (6 - 6) ** 2 + (7 - 6) ** 2) / 3) ** 0.5)

    def test_desviacion_estandar_todos_ceros(self):
        datos = DesviacionEstandar([0, 0, 0, 0, 0])
        self.assertEqual(datos.calcular_desviacion(), "Cero")

    def test_desviacion_estandar_numeros_mixtos(self):
        datos = DesviacionEstandar([1, -3, 8])
        self.assertEqual(datos.calcular_desviacion(), (((1 - 2) ** 2 + (-3 - 2) ** 2 + (8 - 2) ** 2) / 3) ** 0.5)

    def test_desviacion_estandar_elementos_no_numericos(self):
        datos = DesviacionEstandar(["a", "b,", "c", "d"])
        self.assertEqual(datos.calcular_desviacion(), "TypeError")
