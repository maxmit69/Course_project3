# fprint(my_date[0])
# for i in my_date:
#    print(i['date'])
#    print(i['description'])
#    print(f" Со счёта {i.get('from')}")
#   print(f" На {i['to']}")
#  print(i['operationAmount']['amount'])
# print(i['operationAmount']['currency']['name'])

# def masking_the_card_number(number_card: str) -> str:
#    n = 4
#    str_split = number_card.split()
#    str_number2 = str_split.pop()
#    new_number = str_number2[:6] + '*' * 6 + str_number2[-4:]
#    new_number = [new_number[i:i+n] for i in range(0, len(new_number), n)]
#    new_number = ' '.join(new_number)
#    str_split.append(new_number)
#    str_numb_card = ' '.join(str_split)
#    return str_numb_card


from__ = 'Visa Classic 6831982476737658'


# y = from__.split()
# print(y[1])


def masking_the_card_number2(number_card: str) -> str:
    n = 4
    str_split = number_card.split()
    str_number2 = str_split.pop()
    new_number = str_number2[:0] + '*' * 2 + str_number2[-4:]
    new_number = [new_number[i:i + n] for i in range(0, len(new_number), n)]
    new_number = ''.join(new_number)
    str_split.append(new_number)
    str_numb_card = ' '.join(str_split)
    return str_numb_card


print(masking_the_card_number2(from__))
