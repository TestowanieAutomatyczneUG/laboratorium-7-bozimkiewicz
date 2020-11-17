import unittest
from src.sample.Hamming import *
from parameterized import parameterized, parameterized_class


class HammingParameterizedPackage(unittest.TestCase):
    def setUp(self):
        self.tmp = Hamming()

    @parameterized.expand([
        ('A', 'A', 0),
        ('G', 'T', 1),
        ('GGACGGATTCTG', 'AGGACGGATTCT', 9),
    ])
    def test_one_parameterized(self, first, second, expected):
        self.assertEqual(self.tmp.distance(first, second), expected)


@parameterized_class(('first', 'second', 'expected'), [
        ('A', 'A', 0),
        ('G', 'T', 1),
        ('GGACGGATTCTG', 'AGGACGGATTCT', 9),
])
class HammingParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Hamming()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.distance(self.first, self.second), self.expected)


if __name__ == '__main__':
    unittest.main()
