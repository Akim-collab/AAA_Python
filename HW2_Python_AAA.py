import json
import keyword


class ParsingJson:
    """
    A separate class that will convert JSON objects to python-objects with dotted attribute access
    and that will be used to parse the declaration fields and the nested location field.

    ...

    Attributes
    __________

    mapping : str or dict
        An object with nested fields for parsing.

    Methods
    _______

    compute_attr_value(value):
        Method for parsing nested objects.
    """

    def __init__(self, mapping):
        if type(mapping) is str:
            dict_mapping = json.loads(mapping)

            assert 'title' in dict_mapping.keys(), "The required \"title\" field is missing"

            if 'price' in dict_mapping.keys():
                if dict_mapping['price'] < 0:
                    raise ValueError("must be >= 0")
            else:
                dict_mapping['price'] = 0

        else:
            dict_mapping = dict(mapping)

        for key, value in dict_mapping.items():
            if keyword.iskeyword(key):
                key = key + '_'
            setattr(self, key, ParsingJson.compute_attr_value(value))

    @staticmethod
    def compute_attr_value(value):
        if type(value) is dict:
            return ParsingJson(value)
        else:
            return value


class ColorizeMixin:
    """
    Mixin class to change output color Advert.__repr__
    """

    def __str__(self) -> str:
        self.repr_color_code = input("Введите номер цвета: ")
        return f'\033[{self.repr_color_code}m{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, ParsingJson):
    """
    The main class for processing JSON objects.
    """

    def __repr__(self) -> str:
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    pass
