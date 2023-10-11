from choice_file import choice_number_file


def delete_row():
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
        del data[number_row - 1]
        data = [
            f'{i + 1};{data[i].split(";")[1]};'
            f'{data[i].split(";")[2]};'
            f'{data[i].split(";")[3]};'
            f'{data[i].split(";")[4]}'
            for i in range(len(data))
        ]
        with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        print('line deleted successfully')
