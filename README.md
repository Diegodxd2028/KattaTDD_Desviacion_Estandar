# PROYECTO DESVIACIÓN ESTÁNDAR
## DESCRIPCIÓN
Este proyecto está diseñado para calcular la desviación estándar de una lista de valores numéricos en Python. Incluye clases y excepciones personalizadas para manejar distintos tipos de listas, validando que los datos ingresados sean numéricos. También se proporciona una clase para calcular el promedio de la lista, el cual es utilizado como parte del cálculo de la desviación estándar. La desviación estándar ayuda a medir la variabilidad de los datos respecto al promedio, mostrando qué tan dispersos están los valores en una lista.
## Descripción de Archivos
### DesviacionEstandar.py:

Define la clase DesviacionEstandar, que calcula la desviación estándar de una lista de números dada.
Incluye verificación para manejar listas vacías y valores no numéricos.
Si todos los valores son cero, devuelve "Cero".
### Promedio.py:

Define la clase Promedio, que calcula el promedio de una lista de números.
La clase valida que los datos sean numéricos y que la lista no esté vacía.
Si todos los valores son cero, devuelve "Cero".
### prueba.py:

Incluye pruebas unitarias que evalúan los distintos casos posibles, como listas vacías, listas de un solo elemento, listas con números negativos y positivos, y listas con valores no numéricos.
Las pruebas aseguran que las clases y los métodos devuelvan resultados esperados para cada tipo de entrada.

## INTEGRANTES
| Apellidos y nombres| ROL |
|--------------------|-----|
|ARROYO RAMÍREZ, Billy Patrick| Desarrollador |
|CURI UNTIVEROS, Jefferson Diego| Desarrollador |

# Resultados Esperados
## Ejecutar las pruebas unitarias:
### Pruebas de Promedio (Promedio.py):

Listas vacías: Se espera que el método calcular_media devuelva None.
Un solo elemento: El promedio es el mismo valor que el elemento.
Varios elementos: Calcula el promedio correcto.
Todos los elementos son cero: Devuelve "Cero".
Elementos no numéricos: Devuelve "TypeError".
### Pruebas de Desviación Estándar (DesviacionEstandar.py):

Lista vacía: Devuelve None.
Un solo elemento: Devuelve 0 (no hay variabilidad).
Dos o más elementos: Calcula correctamente la desviación estándar según la fórmula.
Todos los elementos son cero: Devuelve "Cero".
Elementos no numéricos: Devuelve "TypeError".
## Interpretación de Resultados
Los resultados mostrarán la variabilidad en los datos proporcionados. Un valor de desviación estándar alto indica que los datos están dispersos alrededor del promedio, mientras que un valor bajo indica que los datos están más concentrados cerca del promedio. En el contexto del proyecto, estos cálculos pueden ser útiles para analizar la dispersión en conjuntos de datos en aplicaciones prácticas.
