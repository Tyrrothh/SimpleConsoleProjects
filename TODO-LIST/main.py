from rich.console import Console
from os import system

console = Console()


def is_task_exist(tasks_list: list, number_of_task: int) -> bool:
    if len(tasks_list) == 0:
        return False
    else:
        return 1 <= number_of_task <= len(tasks_list)


def display_menu() -> None:
    console.print('=================== MENU ===================', style='bold #994C00')
    console.print('[1] Display tasks', style='#994C00')
    console.print('[2] Add task', style='#994C00')
    console.print('[3] Delete task', style='#994C00')
    console.print('[4] Mark the task as completed', style='#994C00')
    console.print('[5] Exit', style='#994C00')
    console.print('=================== MENU ===================', style='bold #994C00')


def display_tasks(tasks_list: list) -> None:
    console.print('\n================ TASKS ================', style='bold #994C00')
    if len(tasks_list) == 0:
        console.print("No tasks", style='bold red')
    else:
        for index, task in enumerate(tasks_list):
            console.print(f'[{index + 1}] -> {task}', style='#FF9933')
    console.print('================ TASKS ================\n', style='bold #994C00')


def add_task(tasks_list: list, task_content: str) -> None:
    tasks_list.append(task_content)
    console.print('Task successfully added!\n', style='bold green')


def delete_task(tasks_list: list, number_of_task: int) -> None:
    if is_task_exist(tasks_list, number_of_task):
        del tasks_list[number_of_task - 1]
        console.print('Task successfully deleted!\n', style='bold green')
    else:
        console.print('Invalid Value!\n', style='bold red')


def mark_the_task_as_completed(tasks_list: list, number_of_task: int) -> None:
    if is_task_exist(tasks_list, number_of_task):
        task_content = tasks_list[number_of_task - 1]

        tasks_list[number_of_task - 1] = '[*] ' + task_content
        console.print('Task successfully marked as completed!\n', style='bold green')
    else:
        console.print('Invalid Value!\n', style='bold red')


def main():
    tasks_list = []

    while True:
        display_menu()
        user_choice = int(input('Enter your choice: '))

        if user_choice != 1:
            system('cls')

        if user_choice == 1:
            display_tasks(tasks_list)

        elif user_choice == 2:
            task_content = input('\nEnter your task: ')
            if len(task_content) >= 3:
                add_task(tasks_list, task_content)
            else:
                console.print('The task content must contain at least 3 characters!\n', style='bold #FF8000')

        elif user_choice == 3:
            number_of_task = int(input('\nEnter the task number: '))
            delete_task(tasks_list, number_of_task)

        elif user_choice == 4:
            number_of_task = int(input('\nEnter the task number: '))
            mark_the_task_as_completed(tasks_list, number_of_task)

        elif user_choice == 5:
            exit(0)

        else:
            console.print('Invalid Value!\n', style='bold red')


if __name__ == '__main__':
    main()
