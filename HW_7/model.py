from csv import reader

# 1 - Показать справочник
def show_book():
    with open('phonebook.csv', 'r', encoding='UTF-8') as file:
        file_content = file.read()
        if len(file_content) == 0:
            print('В справочнике нет контактов')
        else:
            print(file_content)


# 2 - Добавить контакт
def add_contact():
    global contact_details
    id_contact = input('Введите ИД контакта: ')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    birth_date = input('Дату рождения в формате ДД/ММ/ГГГГ :')
    place_of_work = input('Введите место работы: ')
    phone_number = input('Введите номер телефона в формате +71231234567: ')
    type_of_phone_number = input('Введите тип телефона: ')
    contact_details = (
        f'{id_contact},{last_name},{first_name},{birth_date},{place_of_work},{phone_number},{type_of_phone_number}\n')
    with open('phonebook.csv', 'a+', encoding='UTF-8') as file:
        file.write(contact_details)
    print(f'Добавлена запись {contact_details}')
    return contact_details


# 3 - Найти контакт
def search_contact():
    global search_result
    search_last_name = input('Введите Фамилию для поиска: ')
    search_first_name = input('Введите имя для поиска: ')

    with open('phonebook.csv', 'r+', encoding='UTF-8') as file:
        file_contents = file.readlines()
        found = False
        full_name = (search_last_name + ',' + search_first_name).lower()
        for line in file_contents:
            if full_name in line.lower():
                print(f'Найден контакт: {line}')
                found = True
                ans = input('Искать дальше Нет - 2, Да - Enter: ')
                if ans == 2:
                    break
        if found == False:
            print(f'Контакт - {search_last_name} {search_first_name} не найден')
    search_result = search_last_name + ' ' + search_first_name
    return search_result


# 4 - Удалить контакт

def delete_contact():
    global delete_result
    show_book()
    with open('phonebook.csv', 'r', encoding='UTF-8') as file:
        csv_contents = reader(file)
        list_of_rows = list(csv_contents)
        delete_id = input('Введите ИД строки, которую хотите удалить: ')
    with open('phonebook.csv', 'w', encoding='UTF-8') as file:
        for line in list_of_rows:
            if line[0] != delete_id:
                lst = ','.join(str(item) for item in line)
                file.write(lst + '\n')
    delete_result = print(f'Контакт с ИД = {delete_id} удален')
    return delete_result