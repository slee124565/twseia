import unittest


def test():
    tests = unittest.TestLoader().discover('./tests', pattern='test*.py')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    return 0 if results.wasSuccessful() else 1


test()
