from delete_data import delete_row
from change_data import change_row
from add_data import add_row
from print_data import print_file


def verify_command(command):
    while command < 1 or command > 5:
        command = int(
            input(
                "Error! command not found. Please, try again. "
                "Use from 1 to 5 numbers for choosing\n"
                "Hi there!\n"
                "choose the function:\n"
                "1. Add\n"
                "2. Delete\n"
                "3. Change\n"
                "4. Output\n"
                "5. Quit\n"
                "Enter command number: "
            )
        )
    return command


def start_menu():
    print("Hi there!\n")
    command = None
    while command != 5:
        command = int(
            input(
                "choose the function:\n"
                "1. Add\n"
                "2. Delete\n"
                "3. Change\n"
                "4. Output\n"
                "5. Quit\n"
                "Enter command number: "
            )
        )
        command = verify_command(command)
        if command == 1:
            add_row()
        elif command == 2:
            delete_row()
        elif command == 3:
            change_row()
        elif command == 4:
            print_file()
    print("Thanks for using! We hope to see you soon! Bye!")
