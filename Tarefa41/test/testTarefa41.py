import math

def calcular_area_circulo(radio):
  
    areacirculo = math.pi * radio**2
    return areacirculo

def calcular_volumen_cilindro(radio, altura):

    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen
