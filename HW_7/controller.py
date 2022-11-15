import view
import model
import logger


def run():
    while True:
        view.show_menu()
        answer = input('Ваш выбор :')

        match answer:
            case '1':   # 1 - Показать справочник
                result = model.show_book()
            case '2':   # 2 - Добавить контакт
                pass
            case '3':   # 3 - Редактировать контакт
                pass
            case '4':   # 4 - Удалить контакт
                pass
            case '5':   # 5 - Загрузить справочник
                pass
            case '6':   # 6 - Сохранить справочник
                pass
            case '7':   # 7 - Выход
                exit()

        # view.show(result)
        logger.calculation_logger(result, answer)