import unittest
import full_name


class SimpleTest(unittest.TestCase):
    def test_full_name_1(self):
        self.assertEqual(full_name.full_n("Wonjun", "Roh"), "Wonjun Roh")

    def test_full_name_2(self):
        self.assertEqual(full_name.full_n("Wonjun", 3), "Input must be string")

    def test_full_name_3(self):
        self.assertEqual(full_name.full_n(
            "Wonjun", ""), "Input is empty string")


if __name__ == '__main__':
    unittest.main()
