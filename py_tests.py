import sys
import unittest
from twseia.taiseia101 import *

if __name__ == '__main__':
    tests = unittest.TestLoader().discover('./tests', pattern='test*.py')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    sys.exit(0 if results.wasSuccessful() else 1)
    # print(f'{RegisterRequest().to_pdu()}')
