from rich.console import Console
from os import system


console = Console()


class Account:
    def __init__(self) -> None:
        self.balance: int = 0
        self.transactions: list = []

    def print_balance(self) -> None:
        console.print('\n=========================', style='bold #994C00')
        console.print(f'Current Balance: {self.balance} PLN', style='bold #FF9933')
        console.print('=========================\n', style='bold #994C00')

    def print_transaction(self) -> None:
        console.print('\n=================== TRANSACTIONS ===================', style='bold #994C00')
        if len(self.transactions) > 0:
            for index, transaction in enumerate(self.transactions):
                console.print(f'[{index + 1}] {transaction}', style='italic #FF9933')
        else:
            console.print('You have no transactions!', style='bold #FF9933')
        console.print('=================== TRANSACTIONS ===================\n', style='bold #994C00')

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.balance += amount
            self.transactions.append(f'DEPOSIT -> {amount} PLN')
            console.print(f'Deposit of {amount} PLN successful!', style='bold green')
            console.print('=====================================\n', style='bold #994C00')
        else:
            console.print('Invalid Value!', style='bold red')
            console.print('=====================================\n', style='bold #994C00')

    def withdraw(self, amount: int) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'WITHDRAW -> {amount} PLN')
            console.print(f'Withdrawal of {amount} PLN successful!', style='bold green')
            console.print('=====================================\n', style='bold #994C00')
        else:
            console.print('Invalid Value!', style='bold red')
            console.print('=====================================\n', style='bold #994C00')


def print_menu() -> None:
    console.print('================= MENU =================', style='bold #994C00')
    console.print('[1] Display funds', style='#994C00')
    console.print('[2] Deposit', style='#994C00')
    console.print('[3] Withdraw', style='#994C00')
    console.print('[4] Transactions', style='#994C00')
    console.print('[5] Exit', style='#994C00')
    console.print('================= MENU =================', style='bold #994C00')


def main():
    account = Account()

    while True:
        print_menu()
        user_choice = int(input('Enter your choice: '))
        system('cls')

        if user_choice == 1:
            account.print_balance()
        elif user_choice == 2:
            console.print('\n=====================================', style='bold #994C00')
            amount: int = int(input('Enter amount deposit: '))
            account.deposit(amount)
        elif user_choice == 3:
            console.print('\n=====================================', style='bold #994C00')
            amount: int = int(input('Enter amount withdraw: '))
            account.withdraw(amount)
        elif user_choice == 4:
            account.print_transaction()
        elif user_choice == 5:
            exit(0)
        else:
            console.print('Invalid Value!', style='bold red')


if __name__ == '__main__':
    main()
