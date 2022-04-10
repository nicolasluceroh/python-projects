def palindrome(word):
    return word == word[::-1]


def run():
    word = str(input("Type a word: ")).lower().replace(' ', '')
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("Is palindrome")
    else:
        print("Is not a palindrome")



if __name__ == '__main__':
    run()