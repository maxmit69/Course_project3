import os.path
import pytest
from course_project3 import utils
from config import ROOT_DIR


@pytest.fixture
def test_heck_data():
    return [{"a": 1}, {"a": 2, "b": 3}]


def test_utils_validation_check(test_heck_data):
    assert utils.validation_check(test_heck_data) == [{"a": 1}, {"a": 2, "b": 3}]
    assert utils.validation_check([]) == []
    assert utils.validation_check([{"a": 1}, {}, {"a": 2, "b": 3}]) == [{"a": 1}, {"a": 2, "b": 3}]


def test_reading_json():
    date = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    assert utils.reading_json(data_file=date) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_converts_time():
    assert utils.converts_time('2020-01-01T00:00:00.000000') == '01 01 2020'
    assert utils.converts_time('2024-07-09T00:00:00.003040') == '09 07 2024'
    assert utils.converts_time('2022-12-05T00:00:00.020050') == '05 12 2022'


def test_masking_the_card_number():
    assert utils.masking_the_card_number('Visa Gold 8326537236216459') == 'Visa Gold 8326 53** ****6459'
    assert utils.masking_the_card_number('None') == 'Нет данных'
    assert utils.masking_the_card_number('МИР 5211277418228469') == "МИР 5211 27** ****8469"


def test_masking_the_card_number2():
    assert utils.masking_the_card_number2('Счет 58518872592028002662') == 'Счет **2662'
    assert utils.masking_the_card_number2('Счет 20735820461482021315') == 'Счет **1315'
    assert utils.masking_the_card_number2('МИР 5211277418228469') == "МИР **8469"


def test_sorts_dict_with_time():
    assert utils.sorts_dict_with_time([{'date': '2019-05-19T12:51:49.023880', 'state': 'EXECUTED'},
                                       {'date': '2018-12-24T20:16:18.819037', 'state': 'EXECUTED'}]) == {
               '19 05 2019': 'EXECUTED',
               '24 12 2018': 'EXECUTED'}
