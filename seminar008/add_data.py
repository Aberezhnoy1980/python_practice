from choice_file import choice_number_file


def add_row():
    nf = choice_number_file()
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    date_of_birth = input("Enter date of birth: ")
    location = input("Enter your location: ")
    with open(f"db/data_{nf}.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        now_number_row = len(data) + 1
    with open(f"db/data_{nf}.txt", "a", encoding="utf-8") as file:
        file.write(f"{now_number_row};{name};{surname};{date_of_birth};{location}\n")
    print('Data added successfully')
