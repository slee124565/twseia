import sys
import unittest
import twseia

# from tests.sample_pdus import *

sys.path.append('.')


class TestSmartApplication(unittest.TestCase):

    def test_read_service(self):
        raise NotImplementedError
        # pass

    def test_write_service(self):
        raise NotImplementedError
        # pass

    def test_register(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
