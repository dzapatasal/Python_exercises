"""Vamos a practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

Calentamiento

1 - Escribe un código que lee la lista siguiente y realiza:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# 1. Leer el tamaño de la lista
# 2. Leer el valor máximo y mínimo
# 3. Calcular la suma de los valores de la lista
# 4. Mostrar un mensaje al final: La lista tiene `tamano` números, donde el mayor 
# es `mayor` y el menor es `menor`. La suma de los valores es `suma`.
Copia el código
2 - Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 7, la tabla de multiplicar se debe mostrar en el siguiente formato:

# Tabla del  7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70
Copia el código
3 - Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
Copia el código
4 - Crea una lista de los cuadrados de los números de la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Recuerda utilizar las funciones lambda y map() para calcular el cuadrado de cada elemento de la lista.

Aplicando a proyectos

5 - Has sido contratado como científico(a) de datos de una asociación de skate. Para analizar las notas recibidas por los skaters en algunas competiciones a lo largo del año, necesitas crear un código que calcule la puntuación de los atletas. Para ello, tu código debe recibir 5 notas ingresadas por los jueces.

6 - Para cumplir con una demanda de una institución educativa para el análisis del rendimiento de sus estudiantes, necesitas crear una función que reciba una lista de 4 notas y devuelva:

# mayor nota
# menor nota
# media
# situación (Aprobado(a) o Reprobado(a))
# Uso de la función
# Mostrar: El estudiante obtuvo una media de `media`, con la mayor nota de `mayor` puntos y la menor nota de `menor` puntos y fue `situacion`.)
Copia el código
7 - Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante concatenándolos para presentar sus nombres completos en la forma Nombre Apellido. Las listas son:

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
# Puedes apoyarte en la función map()
Copia el código
8 - Como científico de datos en un equipo de fútbol, necesitas implementar nuevas formas de recopilación de datos sobre el rendimiento de los jugadores y del equipo en su conjunto. Tu primera acción es crear una forma de calcular la puntuación del equipo en el campeonato nacional a partir de los datos de goles marcados y recibidos en cada juego.

Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas de números enteros, representando los goles marcados y recibidos por el equipo en cada partido del campeonato. La función debe devolver la puntuación del equipo y el rendimiento en porcentaje, teniendo en cuenta que la victoria vale 3 puntos, el empate 1 punto y la derrota 0 puntos.

Nota: si la cantidad de goles marcados en un partido es mayor que los recibidos, el equipo ganó. En caso de ser igual, el equipo empató, y si es menor, el equipo perdió. Para calcular el rendimiento, debemos hacer la razón entre la puntuación del equipo y la puntuación máxima que podría recibir.

Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:

goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]
# Texto probablemente mostrado:
# La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"
Copia el código
9 - Te han desafiado a crear un código que calcule los gastos de un viaje a una de las cuatro ciudades desde Recife, siendo ellas: Salvador, Fortaleza, Natal y Aracaju.

El costo diario del hotel es de 150 reales en todas ellas y el consumo de gasolina en el viaje en coche es de 14 km/l, siendo que el precio de la gasolina es de 5 reales por litro. Los gastos con paseos y alimentación a realizar en cada una de ellas por día serían [200, 400, 250, 300], respectivamente.

Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente [850, 800, 300, 550] km, crea tres funciones: la primera función calcula los gastos de hotel (gasto_hotel), la segunda calcula los gastos de gasolina (gasto_gasolina) y la tercera los gastos de paseo y alimentación (gasto_paseo).

Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta en coche.

# Texto probablemente mostrado:
# Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde 
# Recife costaría [gastos] reales.
Copia el código
10 - Has comenzado una pasantía en una empresa que trabaja con procesamiento de lenguaje natural (NLP). Tu líder te solicitó que crees un fragmento de código que reciba una frase escrita por el usuario y filtre solo las palabras con un tamaño mayor o igual a 5, mostrándolas en una lista. Esta demanda se centra en el análisis del patrón de comportamiento de las personas al escribir palabras de esta cantidad de caracteres o más.

Consejo: utiliza las funciones lambda y filter() para filtrar estas palabras. Recordando que la función integrada filter() recibe una función (en nuestro caso, una función lambda) y filtra un iterable según la función. Para tratar la frase, utiliza replace() para cambiar ',' '.', '!' y '?' por espacio.

Utiliza la frase "Aprender Python aquí en Alura es muy bueno" para probar el código.
"""
