import random

Num_Digits = 3
Max_Guesses = 10

def main():
    print(f'''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    
    I am thinking of a {Num_Digits}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
        Pico         One digit is correct but in the wrong position.
        Fermi        One digit is correct and in the right position.
        agels       No digit is correct.
    
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.''')

    while True:
        secretnumber = getsecretNum()
        print("Eu decidi um numero")
        print(f"Você tem {Num_Digits} tentativas para acerta-lo.")

        num_guesses = 1

        while num_guesses <= Max_Guesses:
            guess = ''
            while len(guess) != Num_Digits or not guess.isdigit():
                print(f'Guess #{num_guesses}')
                guess = input("> ")

            clues=getClues(guess, secretnum)
            print(clues)
            num_guesses += 1

            if guess == secretnumber:
                break
            if num_guesses > Max_Guesses:
                print("You ran out of guesses.")
                print(f"The aswner was {secretnumber}")
            print('Do you want to play again ? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
print("Thanks for playing")
print("See you soon!")