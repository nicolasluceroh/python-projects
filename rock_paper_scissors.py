import random



menu = '''
Welcome to Rock, Paper, Scissors

    [1] Rock
    [2] Paper
    [3] Scissors
   
Select an option: '''

menu_tie = '''
Tie! Let's keep playing

    [1] Rock
    [2] Paper
    [3] Scissors
   
Select an option: '''

def console_option():
    console = random.randint(1, 3)
    
    if console == 1:
        print("Console choose Rock")
    elif console == 2:
        print("Console choose Paper")
    elif console == 3:
        print("Console choose Scissors")
    
    return console

def run():
    option = int(input(menu))
    console = console_option()
    
    while console == option:
        option = 0
        option = int(input(menu_tie))
        console = console_option()
    if console == 1 and option == 2:
        print("You win!")
    elif console == 2 and option == 3:
        print("You win!")
    elif console == 3 and option == 1:
        print("You win!")
    elif option == 1 and console == 2:
        print("You have lost!")
    elif option == 2 and console == 3:
        print("You have lost!")
    elif option == 3 and console == 1:
        print("You have lost!")
    else:
        print("Enter a correct option")
        option = int(input(menu))
        console = console_option()

if __name__ == '__main__':
    run()
