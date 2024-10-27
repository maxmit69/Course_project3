import json
from datetime import datetime


def reading_json(data_file: json) -> list:
    """ Чтение файла с данными из json
    :param data_file: Файл json
    :return: Данные из json
    """
    with open(data_file, encoding="utf=8") as file:
        return json.load(file)


def validation_check(file_name: list) -> list:
    """ Проверка наличия данных в файле
    :param file_name: Данные из json
    :return: Валидные данные
    """
    valid_date = []
    for elem in file_name:
        if elem == {} or elem is None:
            continue
        else:
            valid_date.append(elem)
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
        str_split = num_card.split()
        str_number = str_split.pop()
        new_number = f'{str_number[:4]} {str_number[4:6]}** ****{str_number[-4:]}'
        str_split.append(new_number)
        return ' '.join(str_split)
    else:
        return f'Нет данных'


def masking_the_card_number2(number_card: str) -> str:
    """ Конвертирует строку в список,
    из списка выхватывает номером карты преобразует и вставляет обратно.
    :param number_card: Номер карты или счета
    :return: Замаскированный номер
    """
    str_split = number_card.split()
    str_number = str_split.pop()
    new_number = f'**{str_number[-4:]}'
    str_split.append(new_number)
    return ' '.join(str_split)


def sorts_dict_with_time(file_date: list) -> dict:
    """ Сортировка даты по убыванию
    :param file_date: Дата из json по ключу 'date'
    :return: Отсортированная дата
    """
    date_sort = []
    execute_state = []
    for item in file_date:
        date_sort.append(converts_time(item['date']))
        execute_state.append(item['state'])
    sort_data: list[str] = sorted(date_sort, key=lambda x: (x.split()[2], x.split()[1], x.split()[0]), reverse=True)
    sort_dict = dict(zip(sort_data, execute_state))
    return sort_dict

