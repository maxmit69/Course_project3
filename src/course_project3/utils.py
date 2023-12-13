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
print(len(date_bank))
my_date = []
for i in date_bank:
    if i == {}:
        continue
    else:
        my_date.append(i)


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
    Возвращает строку
    :param num_card: Номер карты
    :return: Замаскированный номер карты
    """
    if not 'None' == num_card:
        n = 4
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
    Возвращает строку
    :param number_card: Номер карты
    :return: Замаскированный номер карты
    """
    n = 4
    str_split = number_card.split()
    str_number2 = str_split.pop()
    new_number = str_number2[:0] + '*' * 2 + str_number2[-4:]
    new_number = [new_number[i:i + n] for i in range(0, len(new_number), n)]
    new_number = ''.join(new_number)
    str_split.append(new_number)
    str_numb_card = ' '.join(str_split)
    return str_numb_card


data_ = []
description_ = []
from_num_card = []
to_num_card = []
money = []
currency_ = []
for i in my_date:
    data_.append(converts_time(i['date']))
    description_.append(i['description'])
    from_num_card.append(masking_the_card_number(i.get('from', str(None))))
    to_num_card.append(masking_the_card_number2(i['to']))
    money.append(i['operationAmount']['amount'])
    currency_.append(i['operationAmount']['currency']['name'])


print(data_)
print(description_)
print(from_num_card)
print(to_num_card)
print(money)
print(currency_)
