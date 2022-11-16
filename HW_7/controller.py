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
                result = model.search_result
            case '4':   # 4 - Удалить контакт
                model.delete_contact()
                result = model.delete_result
            case '5':   # 5 - Загрузить справочник
                pass
            case '6':   # 6 - Сохранить справочник
                pass
            case '7':   # 7 - Выход
                exit()

        # view.show(result)
        logger.calculation_logger(result, answer)