import json
import os
from datetime import datetime

content = os.path.join(r'/home/vinsen/PycharmProjects/Course_project3/bank_data/', 'operations.json')


def reading_json(path: json) -> list:
    """ Чтение файла с данными из json
    :param path: Путь к файлу
    :return: Данные из json
    """
    with open(path, 'r') as file:
        return json.load(file)


date_bank = reading_json(content)


def validation_check(file_name: list) -> list:
    """ Проверка наличия данных в файле
    :param file_name: Данные из json
    :return: Валидные данные
    """
    valid_date = []
    for item in date_bank:
        if item == {}:
            continue
        else:
            valid_date.append(item)
    return valid_date


def converts_time(time: str) -> str:
    """
    Преобразование формата времени
    """
    time_obj = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f')
    new_time_obj = time_obj.strftime('%d %m %Y')
    return new_time_obj


def masking_the_card_number(num_card: str) -> str:
    """ Получает строку и проверяет на наличие данных. Конвертирует строку в список,
    из списка выхватывает номером карты преобразует и вставляет обратно.
    :param num_card: Номер карты или счёта
    :return: Замаскированный номер
    """
    if not 'None' == num_card:
        n: int = 4
        str_split = num_card.split()
        str_number = str_split.pop()
        new_number = str_number[:6] + '*' * 6 + str_number[-4:]
        new_number = [new_number[item:item + n] for item in range(0, len(new_number), n)]
        new_number = ' '.join(new_number)
        str_split.append(new_number)
        str_numb_card = ' '.join(str_split)
        return str_numb_card
    else:
        return f'Нет данных'


def masking_the_card_number2(number_card: str) -> str:
    """ Конвертирует строку в список,
    из списка выхватывает номером карты преобразует и вставляет обратно.
    :param number_card: Номер карты или счета
    :return: Замаскированный номер
    """
    n: int = 4
    str_split = number_card.split()
    str_number2 = str_split.pop()
    new_number = str_number2[:0] + '*' * 2 + str_number2[-4:]
    new_number = [new_number[item:item + n] for item in range(0, len(new_number), n)]
    new_number = ''.join(new_number)
    str_split.append(new_number)
    str_numb_card = ' '.join(str_split)
    return str_numb_card


def sorts_data_with_time(file_name: list) -> list:
    """ Сортировка данных по времени
    :param file_name: Данные из json
    :return: Сортированные данные
    """
    date_sort = []
    for item in file_name:
        date_sort.append(converts_time(item['date']))
        sort_data: list[str] = sorted(date_sort, key=lambda x: (x.split()[2], x.split()[1], x.split()[0]), reverse=True)
    return sort_data
