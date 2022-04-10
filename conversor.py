from ast import If
from lib2to3.pytree import convert


menu = '''
Selecciona que tipo de operacion quieres realizar

    [1] Pesos Argentinos a Dolares
    [2] Dolares a Pesos Argentinos
    [3] Pesos Colombianos a Dolares
    [4] Dolares a Pesos Colombianos
    [5] Dolares a BitCoin 

Selecciona una opcion: '''

operacion = int(input(menu))

valor_dolar_argentina = 202.5
valor_dolar_colombia = 3819.84
valor_bitcoin = 41447.20

def convertir(operacion, cantidad):
    resultado = 0

    if operacion == 1:
        resultado = str(round(cantidad / valor_dolar_argentina, 2))
        print("$" + str(cantidad) + " pesos argentinos son $" + resultado + " dolares." )
    
    elif operacion == 2:
        resultado = str(round(cantidad * valor_dolar_argentina, 2))
        print("$" + str(cantidad) + " dolares son $" + resultado + " pesos argentinos." )

    elif operacion == 3:
        resultado = str(round(cantidad / valor_dolar_colombia, 2))
        print("$" + str(cantidad) + " pesos colombianos son $" + resultado + " dolares." )

    elif operacion == 4:
        resultado = str(round(cantidad * valor_dolar_colombia, 2))
        print("$" + str(cantidad) + " dolares son $" + resultado + " pesos colombianos." )

    elif operacion == 5:
        resultado = str(round(cantidad / valor_bitcoin, 10))
        print("$" + str(cantidad) + " dolares son BTC" + resultado + " bitcoins." )

if operacion >=1 and operacion <= 5:
    cantidad = int(input("Ingresa la cantidad que quieres convertir: "))
    convertir(operacion, cantidad)
else:
    print('''********************************************************
        SELECCIONA UNA OPCION CORRECTA POR FAVOR
********************************************************''')


