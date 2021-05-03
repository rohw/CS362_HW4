import unittest
import volume


class SimpleTest(unittest.TestCase):
    def test_vol_1(self):
        self.assertEqual(volume.vol(2), 8)

    def test_vol_2(self):
        self.assertEqual(volume.vol(-2), 'Positive numbers only')

    def test_vol_3(self):
        self.assertEqual(volume.vol(2.5), 15.625)

    def test_vol_4(self):
        self.assertEqual(volume.vol('hi'), 'Numbers only')


if __name__ == '__main__':
    unittest.main()
