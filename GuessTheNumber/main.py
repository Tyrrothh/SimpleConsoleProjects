from random import randint
from time import sleep
from os import system
from rich.console import Console

console = Console()


def print_a_welcome_message() -> None:
    console.print('=========================== GUESS NUMBER GAME ===========================', style='bold #D16E0A')
    console.print('Welcome, your task is to guess a number within the range [1-100].\n'
                  'You have 5 attempts to guess the correct number! Good Luck!', style='#D16E0A')
    console.print('=========================== GUESS NUMBER GAME ===========================', style='bold #D16E0A')


def main():
    while True:
        print_a_welcome_message()
        sleep(5)
        user_answer: str = input("Enter 'start' to begin the game: ").lower()
        system('cls')

        if user_answer == 'start':
            generated_number: int = randint(1, 100)
            number_of_lives: int = 5

            while number_of_lives > 0:
                user_number: int = int(input('\nEnter the number [1-100]: '))
                system('cls')
                sleep(1)

                if user_number > generated_number:
                    console.print('The provided number is too large', style='italic #F5FC31')
                    number_of_lives -= 1
                    continue
                elif user_number < generated_number:
                    console.print('The provided number is too small', style='italic #F5FC31')
                    number_of_lives -= 1
                    continue
                elif user_number == generated_number:
                    system('cls')
                    console.print(f"Congratulations! You've successfully guessed the correct number!"
                                  f" The correct number was {generated_number}!", style='bold green')
                    break

            if number_of_lives == 0:
                system('cls')
                console.print(f"You've exhausted all attempts, failed to guess the number!"
                              f" The correct number was {generated_number}", style='bold red')

            new_game: str = input("Do you want to play again? [Y | N]: ").upper()
            if new_game == 'Y':
                system('cls')
                continue
            else:
                break

        else:
            exit(211)


if __name__ == '__main__':
    main()
