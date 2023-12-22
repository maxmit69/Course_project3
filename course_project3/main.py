from utils import sorts_dict_with_time, validation_check, converts_time, masking_the_card_number, \
    masking_the_card_number2, reading_json
from config import PATH
import itertools

content = PATH
sort_dict_ = sorts_dict_with_time(validation_check(reading_json(data_file=content)))
sort_dict_ = dict(itertools.islice(sort_dict_.items(), 6))  # Словарь из 5 последних отсортированных данных

if __name__ == '__main__':

    # Сравнивает key('date') и value('state') c отсортированным словарем по дате и "EXECUTED"
    # Выводит данные в нужной по условию последовательности и формату

    for itr in sort_dict_:
        sort_itr_date = itr
        sort_itr_state = sort_dict_[itr]
        for find in validation_check(reading_json(data_file=content)):
            if converts_time(find['date']) == sort_itr_date and find['state'] == sort_itr_state:
                print(f"{(converts_time(find['date']).replace(' ', '.'))} {(find['description'])}\n"
                      f"{(masking_the_card_number(find.get('from', str(None))))} -> "
                      f"{(masking_the_card_number2(find['to']))}\n"
                      f"{find['operationAmount']['amount']} {find['operationAmount']['currency']['name']}\n")
