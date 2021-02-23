import sys
import unittest


if __name__ == '__main__':
    tests = unittest.TestLoader().discover('./tests', pattern='test*.py')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    sys.exit(0 if results.wasSuccessful() else 0)
