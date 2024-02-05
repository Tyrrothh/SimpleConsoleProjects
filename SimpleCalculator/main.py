from rich.console import Console
from os import system

console = Console()


def print_menu():
    console.print('========= MENU =========', style='#BD6711 bold')
    console.print('[1] Addition', style='#BD6711')
    console.print('[2] Subtraction', style='#BD6711')
    console.print('[3] Multiplication', style='#BD6711')
    console.print('[4] Division', style='#BD6711')
    console.print('[5] Exit', style='#BD6711')
    console.print('========= MENU =========', style='#BD6711 bold')


def addition(x: int, y: int) -> int:
    return x + y


def subtraction(x: int, y: int) -> int:
    return x - y


def multiplication(x: int, y: int) -> int:
    return x * y


def division(x: float, y: float) -> float:
    return x / y


def main():
    while True:
        print_menu()
        user_choice = int(input('Select an option [1-5]: '))
        system('cls')

        if user_choice == 1:
            console.print('===================== Addition =====================', style='blue bold')
            x = int(input('Enter the first number: '))
            y = int(input('Enter the second number: '))
            result: int = addition(x, y)
            console.print(f'Result: {result}', style='bold green')
            console.print('===================== Addition =====================\n', style='blue bold')

        elif user_choice == 2:
            console.print('===================== Subtraction =====================', style='blue bold')
            x = int(input('Enter the first number: '))
            y = int(input('Enter the second number: '))
            result: int = subtraction(x, y)
            console.print(f'Result: {result}', style='bold green')
            console.print('===================== Subtraction =====================\n', style='blue bold')

        elif user_choice == 3:
            console.print('===================== Multiplication =====================', style='blue bold')
            x = int(input('Enter the first number: '))
            y = int(input('Enter the second number: '))
            result: int = multiplication(x, y)
            console.print(f'Result: {result}', style='bold green')
            console.print('===================== Multiplication =====================\n', style='blue bold')

        elif user_choice == 4:
            console.print('===================== Division =====================', style='blue bold')
            x = float(input('Enter the first number: '))
            y = float(input('Enter the second number: '))

            if y == 0:
                console.print('Error -> Division by zero!', style='bold red')
            else:
                result: float = division(x, y)
                console.print(f'Result: {result}', style='bold green')
            console.print('===================== Division =====================\n', style='blue bold')

        elif user_choice == 5:
            exit(0)

        else:
            console.print('Invalid Value!\n', style='bold red')


if __name__ == '__main__':
    main()
