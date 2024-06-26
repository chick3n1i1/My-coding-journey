import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Please guess a number between 1 and {x}. '))
        if guess < random_number:
            print("Sorry guess again. You were too low. ")
        elif guess > random_number:
            print("Sorry guess again. You were too high. ")
    print(f"Yay! you guess the number {random_number}. ")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:  # added in case the computer is able get high = low
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(
            f"Is {guess} too High (H), too low (L), or correct (C). ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! the computer guessed your number, {guess} correctly! ")


computer_guess(10)
