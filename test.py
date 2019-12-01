import unittest

class PierwszyTest(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie do testu")
    def test_224(self):
        print
        assert(2+2==4)
    def tearDown(self):
        print("Sprzatam po testach")

if __name__ == '__main__':
    unittest.main(verbosity=2)
