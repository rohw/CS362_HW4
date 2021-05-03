import unittest
import average


class SimpleTest(unittest.TestCase):
    def test_average_1(self):
        self.assertEqual(average.avg([1, 2, 3, 4, 5]), 3)

    def test_average_2(self):
        self.assertEqual(average.avg([1, 2, 3, -3, -2, -1]), 0)

    def test_average_3(self):
        self.assertEqual(average.avg(1), "It's not a list")

    def test_average_4(self):
        self.assertEqual(average.avg([]), "It's an empty list")


if __name__ == '__main__':
    unittest.main()
