from one_hot_encoder import fit_transform
import pytest


def first_base_test():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert exp_transformed_cities == fit_transform(cities)


def test_one_word():
    cities = ['Moscow', 'Moscow', 'Moscow', 'Moscow']
    exp_transformed_cities = [
        ('Moscow', [1]),
        ('Moscow', [1]),
        ('Moscow', [1]),
        ('Moscow', [1]),
    ]
    assert exp_transformed_cities == fit_transform(cities)


def test_empty_list():
    cities = []
    with pytest.raises(TypeError):
        fit_transform(cities)


def second_base_test():
    cities = ['Moscow']
    exp_transformed_cities = [
        ('Moscow', [1, 0])
    ]
    assert exp_transformed_cities == fit_transform(cities)
