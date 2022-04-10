def palindromo(palabra):
    return palabra == palabra[::-1]


def run():
    palabra = str(input("Escribe una palabra: ")).lower().replace(' ', '')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")



if __name__ == '__main__':
    run()