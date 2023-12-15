'''Escribe unha función que reciba coma parámetros
 unha lista e mais unha función, e devolva unha
   nova lista onde cada elemento é o resultado
de aplicares a función ao elemento orixinal da lista.'''

def aplicar_funcion_a_lista(lista, funcion):
    nueva_lista = [funcion(elemento) for elemento in lista]
    return nueva_lista

def calcular_cuadrado(numero):
    return numero ** 2

def calcular_cubo(numero):
    return numero ** 3

# Puedes incluir un ejemplo de uso aquí si lo deseas
numeros = [1, 2, 3, 4, 5]
resultadocuadrado = aplicar_funcion_a_lista(numeros, calcular_cuadrado)
print(resultadocuadrado)

resultadocubo = aplicar_funcion_a_lista(numeros, calcular_cubo)
print(resultadocubo)
