import pytest
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    return area_base * altura

