import view
import model
import logger


def run():
    while True:
        view.show_menu()
        answer = input('Ваш выбор :')

        match answer:
            case '1':   # 1 - Показать справочник
                model.show_book()
                result = 'Просмотр справочника'
            case '2':   # 2 - Добавить контакт
                model.add_contact()
                result = model.contact_details
            case '3':   # 3 - Найти контакт
                model.search_contact()
                result = 'Поиск ' + model.search_result
            case '4':   # 4 - Удалить контакт
                model.delete_contact()
                result = 'Удаление контакта с ИД ' + model.delete_id
            case '5':   # 5 - Загрузить справочник
                model.load_phonebook()
                result = 'Загрузка справочника'
            case '6':   # 6 - Сохранить справочник
                model.save_as_new_file()
                result = 'Файл сохранен под именем' + model.second_file_name
            case '7':   # 7 - Выход
                exit()

        # view.show(result)
        logger.calculation_logger(result, answer)