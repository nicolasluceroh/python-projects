import random


def run():
    num_user = int(input("Choose a number from 1 to 100: "))
    num_console = random.randint(1,100)
    nums_range = [1,100]
    
    res = input("Your number is " + str(num_console) + "? (Y o N): ")

    while num_console != num_user and res.lower() == 'n':
        hint = input("Okay, give me a hint! Is it bigger or smaller (B or S): ")
        if hint.lower() == 'b':
                nums_range[0] = num_console
        elif hint.lower() == 's':
                nums_range[1] = num_console
        num_console = random.randint(nums_range[0]+1, nums_range[1]-1)
        res = input("Your number is " + str(num_console) + "? (Y o N): ")
        if res.lower() == 'y' and num_console != num_user:
            print("Are you sure? I don't think that's your number!")
        elif res.lower() == 'y' and num_console == num_user:
            print("Haha! Very easy! I won!")
        elif res.lower() == 'n' and num_console == num_user:
            print("Mmm, are you sure? I know you're lying! I won!")


if __name__ == '__main__':
    run()