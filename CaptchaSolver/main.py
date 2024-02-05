from random import randint
from time import sleep
from rich.console import Console
from os import system

console = Console()


class Account:
    def __init__(self):
        self.level = 1
        self.experience = 0
        self.balance = 0
        self.rate_per_captcha = 0.00015
        self.correct_captcha = 0
        self.wrong_captcha = 0
        self.all_captcha = 0

    def required_experience(self) -> int:
        return (self.level * 10) + 25

    def level_up(self) -> None:
        if self.experience >= self.required_experience():
            self.experience -= self.required_experience()
            self.level += 1
            self.rate_per_captcha += 0.00001

    def print_account_information(self) -> None:
        console.print(f'Level: {self.level}', style='#994C00')
        console.print(f'Experience: {self.experience} || {self.required_experience()}'
                      f'  [{round((self.experience / self.required_experience()) * 100)}%]', style='#994C00')
        console.print(f'Balance: {self.balance} PLN', style='#994C00')
        console.print(f'Rate per captcha: {self.rate_per_captcha} PLN', style='#994C00')

    def statistics_captcha(self) -> None:
        if self.correct_captcha != 0 and self.wrong_captcha != 0:
            console.print('\n=============== STATISTICS CAPTCHA ===============', style='bold #994C00')
            console.print(
                f'Correct captcha: {self.correct_captcha}     [{round((self.correct_captcha / self.all_captcha) * 100)}%]',
                style='#FFFF00')
            console.print(
                f'Wrong captcha: {self.wrong_captcha}     [{round((self.wrong_captcha / self.all_captcha) * 100)}%]',
                style='#FFFF00')
            console.print(f'All captcha: {self.all_captcha}', style='#FFFF00')
            console.print('=============== STATISTICS CAPTCHA ===============', style='bold #994C00')
        elif self.correct_captcha != 0 and self.wrong_captcha == 0:
            console.print('\n=============== STATISTICS CAPTCHA ===============', style='bold #994C00')
            console.print(
                f'Correct captcha: {self.correct_captcha}     [{round((self.correct_captcha / self.all_captcha) * 100)}%]',
                style='#FFFF00')
            console.print(f'Wrong captcha: {self.wrong_captcha}    [0%]', style='#FFFF00')
            console.print(f'All captcha: {self.all_captcha}', style='#FFFF00')
            console.print('=============== STATISTICS CAPTCHA ===============', style='bold #994C00')
        elif self.wrong_captcha != 0 and self.correct_captcha == 0:
            console.print('\n=============== STATISTICS CAPTCHA ===============', style='bold #994C00')
            console.print(f'Correct captcha: {self.correct_captcha}    [0%]', style='#FFFF00')
            console.print(
                f'Wrong captcha: {self.wrong_captcha}     [{round((self.wrong_captcha / self.all_captcha) * 100)}%]',
                style='#FFFF00')
            console.print(f'All captcha: {self.all_captcha}', style='#FFFF00')
            console.print('=============== STATISTICS CAPTCHA ===============', style='bold #994C00')
        else:
            console.print('\n=============== STATISTICS CAPTCHA ===============', style='bold #994C00')
            console.print('No available statistics', style='bold #FF9933')
            console.print('=============== STATISTICS CAPTCHA ===============', style='bold #994C00')


def generate_captcha() -> str:
    CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    captcha = ''

    for char in range(8):
        char = CHARS[randint(0, len(CHARS) - 1)]
        captcha += char
    return captcha


def print_menu(account: Account) -> None:
    console.print('\n============ CAPTCHA SOLVER MENU ============', style='bold #994C00')
    account.print_account_information()
    console.print('\n[1] Generate Captcha', style='#994C00')
    console.print('[2] Statistics', style='#994C00')
    console.print('[3] Exit', style='#994C00')
    console.print('============ CAPTCHA SOLVER MENU ============\n', style='bold #994C00')


def main():
    account = Account()

    while True:
        print_menu(account)
        user_choice = int(input('Enter your choice: '))
        system('cls')

        if user_choice == 1:
            how_many_captchas = int(input('\nHow many captchas do you want to solve? [1-10]: '))
            system('cls')

            if 1 <= how_many_captchas <= 10:
                for i in range(how_many_captchas):
                    correct_captcha = generate_captcha()
                    sleep(1)
                    console.print('========================', style='bold #0080FF')
                    print(f'CAPTCHA -> {correct_captcha}')
                    user_captcha = input('Enter your captcha: ')
                    sleep(1.25)

                    if user_captcha == correct_captcha:
                        account.all_captcha += 1
                        account.correct_captcha += 1
                        account.experience += 1
                        account.balance += account.rate_per_captcha
                        account.level_up()
                        console.print(f'\nCaptcha solved correctly!', style='bold green')
                        console.print('========================\n', style='bold #0080FF')

                    elif user_captcha != correct_captcha:
                        account.all_captcha += 1
                        account.wrong_captcha += 1
                        console.print(f'\nCaptcha solved wrong!', style='bold red')
                        console.print('========================\n', style='bold #0080FF')

            else:
                console.print('Invalid Value!', style='bold red')

        elif user_choice == 2:
            account.statistics_captcha()

        elif user_choice == 3:
            exit(0)

        else:
            console.print('Invalid Value!', style='bold red')


if __name__ == '__main__':
    main()
