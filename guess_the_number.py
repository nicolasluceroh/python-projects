import random


def run():
    random_number = random.randint(1, 100)
    number_selected = int(input('Choose a number from 1 to 100: '))


    while number_selected != random_number:
        if number_selected < random_number:
            print('Find a higher number')
        else:
            print('Find a smaller number')
        number_selected = int(input('Choose another number: '))
    print('You won!')

if __name__ == '__main__':
    run()