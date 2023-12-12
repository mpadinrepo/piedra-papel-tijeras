
import random

def agente_reactivo(ultima_jugada_oponente):
    opciones = ["piedra", "papel", "tijeras"]

    # Lógica del agente reactivo
    if ultima_jugada_oponente == "piedra":
        return "papel"
    elif ultima_jugada_oponente == "papel":
        return "tijeras"
    elif ultima_jugada_oponente == "tijeras":
        return "piedra"
    else:
        # Elección aleatoria en la primera jugada
        return random.choice(opciones)

