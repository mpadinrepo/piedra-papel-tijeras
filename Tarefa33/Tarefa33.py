""" Tarefa 33

Escribir un programa que pregunte ao usuario os números gañadores da lotería primitiva,
os almacene nunha lista e logo os amose por pantalla ordenados de menor a maior. """

""" cantidad= int(input ('Por favor cuantos numeros de loteria va a grabar? :'))

lista_numeros_loteria=[]

for _ in range(cantidad):
    numeros_de_loteria = int(input("Ingrese numero loteria: "))
    lista_numeros_loteria.append(lista_numeros_loteria)

print (lista_numeros_loteria[:])

 """
cantidad = int(input('Por favor, ¿cuántos números de lotería va a ingresar? :'))

lista_numeros_loteria = []

for _ in range(cantidad):
    numero_de_loteria = int(input("Ingrese número de lotería: "))
    lista_numeros_loteria.append(numero_de_loteria)

lista_numeros_loteria.sort()

print("Números de lotería ordenados de menor a mayor:", lista_numeros_loteria)
