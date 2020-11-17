import unittest
from src.sample.Hamming import *


class HammingParameterizedFile(unittest.TestCase):
    def test_from_file(self):
      fileTest = open("data/hamming_data_test")
      tmpHamming = Hamming()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            first, second, result = data[0], data[1], int(data[2].strip("\n"))
            self.assertEqual(tmpHamming.distance(first, second), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
