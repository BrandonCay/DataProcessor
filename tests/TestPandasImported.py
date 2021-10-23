import unittest

class TestPandasImported(unittest.TestCase):
    def test_importPandas(self):
        try:
            import pandas as pd
        except ImportError:
            print("Pandas Import Error")
            self.fail()

if __name__ == '__main__':
    unittest.main()