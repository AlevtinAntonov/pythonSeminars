def open_file():
    global file_content
    global file
    with open('phonebook.txt', 'a+') as file:
        file_content = file.read()
        return file_content

# 1 - Показать справочник

def show_book():
    open_file()
    if len(file_content) == 0:
        print('В справочнике нет контактов')
    else:
        print(file_content)

# 2 - Добавить контакт
def add_contact():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    birth_date = input('Дату рождения в формате ДД/ММ/ГГГГ :')
    place_of_work = input('Введите место работы: ')
    phone_number = input('Введите номер телефона в формате +71231234567: ')
    type_of_phone_number = input('Введите тип телефона: ')


