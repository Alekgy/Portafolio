import random

def guessing_number():
    number = random.randint(1,100)
    guess = 0
    while guess != number:
        try:
            guess= int(input('Guess one number: '))
            if guess > number:
                print('Choise one number more lower')
        
            elif guess < number:
                print('Choice one number more high')

            else:
                print('You won!')
        
        except ValueError as E :
            print('Choice one valid option!')


if __name__ == '__main__':
    print('Welcome to the game of number guessing!') 
    print('Then guess a number from 1 to 100')
    guessing_number()
