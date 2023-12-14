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
# print(len(date_bank))
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


sort_date = []
for i in my_date:
    sort_date.append(converts_time(i['date']))

sort_date_ = sorted(sort_date, key=lambda x: (x.split()[2], x.split()[1], x.split()[0]), reverse=True)

sort_date_ = sort_date_[0:5]
#print(sort_date_)
data_ = []

n = 3
while n != 0:
    n -= 1

    for i in my_date:
        if converts_time(i['date']) == sort_date_[0]:
            data_.append(converts_time(i['date']).replace(' ', '.'))
            data_.append(i['description'])
            data_.append(masking_the_card_number(i.get('from', str(None))))
            data_.append(masking_the_card_number2(i['to']))
            data_.append(i['operationAmount']['amount'])
            data_.append(i['operationAmount']['currency']['name'])
            sort_date_ = sort_date_[1:] + sort_date_[0:1]

print('', data_[0], data_[1], '\n', data_[2], '->', data_[3], '\n', data_[4], data_[5])
print()
print('', data_[6], data_[7], '\n', data_[8], '->', data_[9], '\n', data_[10], data_[11])
print()
print('', data_[12], data_[13], '\n', data_[14], '->', data_[15], '\n', data_[16], data_[17])
print()
print('', data_[18], data_[19], '\n', data_[20], '->', data_[21], '\n', data_[22], data_[23])
print()
print('', data_[24], data_[25], '\n', data_[26], '->', data_[27], '\n', data_[28], data_[29])
