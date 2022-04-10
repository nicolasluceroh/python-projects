import random


def password_generate():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    characters = MAYUS + MINUS + NUMS + CHARS

    password = []

    for i in range(16):
        random_character = random.choice(characters)
        password.append(random_character)

    password = "".join(password)
    return password

def run():
    password = password_generate()
    print('Tu nueva contraseña es: ' + password)

if __name__ == '__main__':
    run()