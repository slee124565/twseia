import sys
import unittest
from twseia import SmartApplication
from tests.sample_pdus import *

sys.path.append('.')


class TestSmartApplication(unittest.TestCase):

    def test_read_service(self):
        raise NotImplementedError

    def test_write_service(self):
        raise NotImplementedError


if __name__ == '__main__':
    unittest.main()
