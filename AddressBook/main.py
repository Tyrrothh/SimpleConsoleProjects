from rich.console import Console
from rich.table import Table
from os import system


console = Console()


def is_contact_found(contacts: dict, name: str) -> bool:
    return name in contacts.keys()


def display_menu() -> None:
    console.print('=================== MENU ===================', style='bold #994C00')
    console.print('[1] Display contacts', style='#994C00')
    console.print('[2] Find contact', style='#994C00')
    console.print('[3] Add contact', style='#994C00')
    console.print('[4] Delete contact', style='#994C00')
    console.print('[5] Modify contact', style='#994C00')
    console.print('[6] Exit', style='#994C00')
    console.print('=================== MENU ===================', style='bold #994C00')


def display_contacts(contacts: dict) -> None:
    if len(contacts) == 0:
        console.print('\n==================== CONTACTS ====================', style='bold #994C00')
        console.print("You don't have any contacts!", style='bold #FF8000')
        console.print('==================== CONTACTS ====================\n', style='bold #994C00')
    else:
        table_contacts = Table()
        table_contacts.add_column('Contact Name', style='magenta', justify='center')
        table_contacts.add_column('Phone Number', style='green', justify='center')

        for index, (name, phone_number) in enumerate(contacts.items()):
            table_contacts.add_row(name, phone_number)
        console.print(table_contacts)


def find_contact(contacts: dict, name: str) -> None:
    if is_contact_found(contacts, name):
        console.print(f'{name} -> {contacts[name]}\n', style='bold #CCCC00')
    else:
        console.print('The provided contact does not exist!\n', style='bold red')


def add_contact(contacts: dict, name: str, phone_number: str) -> None:
    if not is_contact_found(contacts, name):
        contacts[name] = phone_number
        console.print(f"Contact named '{name}' added successfully!\n", style='bold green')
    else:
        console.print('The provided contact already exists!\n', style='bold red')


def delete_contact(contacts: dict, name: str) -> None:
    if is_contact_found(contacts, name):
        del contacts[name]
        console.print(f"Contact named '{name}' successfully deleted!\n", style='bold green')
    else:
        console.print('The provided contact does not exist!\n', style='bold red')


def modify_contact(contacts: dict, name: str, phone_number: str) -> None:
    if is_contact_found(contacts, name):
        contacts[name] = phone_number
        console.print('\nContact modified successfully!\n', style='bold green')


def main():
    contacts = dict()

    while True:
        display_menu()
        user_choice = int(input('Enter your choice: '))
        if user_choice != 1:
            system('cls')

        if user_choice == 1:
            display_contacts(contacts)

        elif user_choice == 2:
            name = input('\nEnter the contact name: ')
            find_contact(contacts, name)

        elif user_choice == 3:
            name = input('\nEnter the contact name: ')
            phone_number = input('Enter the phone number of the contact: ')

            if 4 <= len(name) <= 12 and len(phone_number) == 9:
                add_contact(contacts, name, phone_number)
            else:
                console.print('\nThe contact name must be between (4-12) characters and the phone number must be 9 digits!\n', style='bold yellow')

        elif user_choice == 4:
            name = input('\nEnter the contact name: ')
            delete_contact(contacts, name)

        elif user_choice == 5:
            name = input('\nEnter the contact name: ')

            if is_contact_found(contacts, name):
                phone_number = input('Please provide a new phone number for this contact: ')

                if len(phone_number) == 9:
                    modify_contact(contacts, name, phone_number)
            else:
                console.print('The provided contact does not exist!\n', style='bold red')

        elif user_choice == 6:
            exit(0)

        else:
            console.print('Invalid Value!\n', style='bold red')


if __name__ == '__main__':
    main()
