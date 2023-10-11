from print_data import print_file


def choice_number_file():
    print_file()
    number = int(input("Choose the file:\n" "Enter 1 or 2: "))
    while number < 1 or number > 2:
        number = int(input("Error!!!\n" "Enter 1 or 2: "))
    return number
