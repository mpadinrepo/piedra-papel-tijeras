""" Tarefa 41

Similar a exercicios anteriores, podes copiar o feito nesa parte e continuar ampliando:
Escribir unha función que calcule a área dun círculo e outra que calcule o volume dun cilindro usando a primeira función.
A area do círculo é pi*r**2
O volume do cilindro é  pi*r**2 * h

Xera test uniatarios, primeiro para a función que calcula a area do circulo, e logo para o volume do cilindro.
radio_circulo = int(input('Escriba cuanto mide el radio del circulo :'))
altura_cilindro = int(input('Escriba cuanto mide la altura del cilindro :'))

def calcular_area_circulo(radio):

    return math.pi * radio**2

def calcular_volumen_cilindro(radio, altura):

    area_base = calcular_area_circulo(radio)
    volumen =  area_base * altura
    return volumen """

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen =  area_base * altura
    return volumen
