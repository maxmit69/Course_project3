from utils import sorts_data_with_time, validation_check, converts_time, masking_the_card_number, \
    masking_the_card_number2, reading_json
from config import PATH

content = PATH

if __name__ == '__main__':
    sort_date_ = sorts_data_with_time(validation_check(reading_json(data_file=content)))
    sort_date_ = sort_date_[0:5]  # Список из 5 последних отсортированных данных
    processed_data = []  # Список с готовыми данными к выводу
    count = 3
    while count != 0:
        count -= 1
        for find in validation_check(reading_json(data_file=content)):  # Валидные данные зи json
            # Сравнивает данные со списком зи 5 последних отсортированных данных
            # Если данные совпадают, то добавляем в список
            if converts_time(find['date']) == sort_date_[0]:
                processed_data.append(converts_time(find['date']).replace(' ', '.'))
                processed_data.append(find['description'])
                processed_data.append(masking_the_card_number(find.get('from', str(None))))
                processed_data.append(masking_the_card_number2(find['to']))
                processed_data.append(find['operationAmount']['amount'])
                processed_data.append(find['operationAmount']['currency']['name'])
                sort_date_ = sort_date_[1:] + sort_date_[0:1]  # Смещение по индексу

    print('', processed_data[0], processed_data[1], '\n', processed_data[2], '->', processed_data[3], '\n',
          processed_data[4], processed_data[5])
    print()
    print('', processed_data[6], processed_data[7], '\n', processed_data[8], '->', processed_data[9], '\n',
          processed_data[10], processed_data[11])
    print()
    print('', processed_data[12], processed_data[13], '\n', processed_data[14], '->', processed_data[15], '\n',
          processed_data[16], processed_data[17])
    print()
    print('', processed_data[18], processed_data[19], '\n', processed_data[20], '->', processed_data[21], '\n',
          processed_data[22], processed_data[23])
    print()
    print('', processed_data[24], processed_data[25], '\n', processed_data[26], '->', processed_data[27], '\n',
          processed_data[28], processed_data[29])
