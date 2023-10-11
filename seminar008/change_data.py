from choice_file import choice_number_file


def change_row():
    nf = choice_number_file()
    with open(f"db/data_{nf}.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        count_rows = len(data)
    if count_rows == 0:
        print("File is empty!")
    else:
        number_row = int(input(f"Enter the row number " f"from 1 to {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(
                input(f"Error!" f"Enter the row number " f"from 1 to {count_rows}: ")
            )
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        date_of_birth = input("Enter date of birth: ")
        location = input("Enter your location: ")
        data[number_row - 1] = f'{number_row};{name};{surname};{date_of_birth};{location}\n'
        with open(f"db/data_{nf}.txt", "w", encoding="utf-8") as file:
            file.writelines(data)
        print('line updated successfully')