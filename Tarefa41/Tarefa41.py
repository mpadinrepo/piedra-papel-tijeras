import pytest
import math

radio_circulo = int(input('Escriba cuanto mide el radio del circulo :'))
altura_cilindro = int(input('Escriba cuanto mide la altura del cilindro :'))

def calcular_area_circulo(radio):

    return math.pi * radio**2

def calcular_volumen_cilindro(radio, altura):

    area_base = calcular_area_circulo(radio)
    volumen =  area_base * altura
    return volumen

