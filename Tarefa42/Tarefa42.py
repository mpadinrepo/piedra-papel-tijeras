# Para esta tarefa imos a precisar:
# - Unha función que aplique un 21% de IVE a unha cantidade
# - Unha función que aplique un 4% de IVE a unha cantidade
# - Unha función que aplique un 10%  de desconto a unha cantidade.

# Finalmente vas a ter unha lista coa lista da compra. Para elemento da lista será un dicionario onde haberá:
# - prezo do produto sen IVE
# - unha función que aplica o desconto... ou None en caso de non ter desconto
# - unha función que calcule o IVE do produto

# Crearás unha función que colla unha cesta da compra e nos devolve o total a pagar, o IVE da compra e máis a cantidade obtida de aplicar os descontos.
# Xera os tes unitarios correspondentes.


def calcular_iva_21(cantidad):
    iva_21 = cantidad * 0.21
    return iva_21
def calcular_iva_04(cantidad):
    iva_04 = cantidad * 0.04
    return iva_04
def aplicar_descuento(cantidad):
    descuento = cantidad * 0.10
    return descuento
def calcular_total_compra(lista_compra):
    total_pagar = 0
    iva_total = 0
    descuento_total = 0

    for producto in lista_compra:
        precio_sin_iva = producto['precio_sin_iva']
        funcion_iva = producto['funcion_iva']
        funcion_descuento = producto['funcion_descuento']

        total_pagar += precio_sin_iva

        if funcion_iva:
            iva_total += funcion_iva(precio_sin_iva)

        if funcion_descuento:
            descuento_total += funcion_descuento(precio_sin_iva)

    total_pagar += iva_total - descuento_total
    return total_pagar, iva_total, descuento_total

# Ejemplo de uso:
lista_compra = [
    {'precio_sin_iva': 100, 'funcion_iva': calcular_iva_21, 'funcion_descuento': aplicar_descuento},
    {'precio_sin_iva': 50, 'funcion_iva': calcular_iva_04, 'funcion_descuento': None},
    # Agrega más productos según sea necesario
]

total, iva, descuento = calcular_total_compra(lista_compra)

print(f'Total a pagar: {total}')
print(f'IVA: {iva}')
print(f'Descuento: {descuento}')
