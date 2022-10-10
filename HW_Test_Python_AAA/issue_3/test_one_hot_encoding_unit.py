from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    def first_base_test(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(exp_transformed_cities, fit_transform(cities))

    def test_one_word(self):
        cities = ['Moscow', 'Moscow', 'Moscow', 'Moscow']
        exp_transformed_cities = [
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1]),
        ]
        self.assertEqual(exp_transformed_cities, fit_transform(cities))

    def test_empty_list(self):
        cities = []
        with self.assertRaises(TypeError):
            fit_transform(cities)

    def second_base_test(self):
        cities = ['Moscow']
        exp_transformed_cities = [
            ('Moscow', [1, 0])
        ]
        self.assertNotEqual(cities, exp_transformed_cities)


if __name__ == '__main__':
    unittest.main()
