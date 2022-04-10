from ast import If
from lib2to3.pytree import convert


menu = '''
Select the type of operation you wish to perform

    [1] Argentine Pesos to Dollars
    [2] US Dollars to Argentine Pesos
    [3] Colombian Pesos to Dollars
    [4] Dollars to Colombian Pesos
    [5] Dollars to BitCoin 

Select an option: '''

operation = int(input(menu))

value_dolar_argentina = 202.5
value_dolar_colombia = 3819.84
value_bitcoin = 41447.20

def convert(operation, quantity):
    result = 0

    if operation == 1:
        result = str(round(quantity / value_dolar_argentina, 2))
        print("$" + str(quantity) + " argentine pesos are $" + result + " dollars." )
    
    elif operation == 2:
        result = str(round(quantity * value_dolar_argentina, 2))
        print("$" + str(quantity) + " dollars are $" + result + " argentine pesos." )

    elif operation == 3:
        result = str(round(quantity / value_dolar_colombia, 2))
        print("$" + str(quantity) + " colombian pesos are $" + result + " dollars." )

    elif operation == 4:
        result = str(round(quantity * value_dolar_colombia, 2))
        print("$" + str(quantity) + " dollars are $" + result + " colombian pesos." )

    elif operation == 5:
        result = str(round(quantity / value_bitcoin, 10))
        print("$" + str(quantity) + " dollars are BTC" + result + " bitcoins." )

if operation >=1 and operation <= 5:
    quantity = int(input("Enter the amount to be converted: "))
    convert(operation, quantity)
else:
    print('''********************************************************
        SELECT A CORRECT OPTION
********************************************************''')


