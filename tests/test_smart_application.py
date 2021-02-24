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

    def test_known_values(self):
        self.assertEqual(twseia._create_payload(
            type_id=0,
            service_id=twseia.SAServiceID.REGISTER.value,
            cmd_id=twseia.SACmdType.READ.value,
            cmd_value=0xffff
        ), [6, 0, 0, 255, 255, 6])


if __name__ == '__main__':
    unittest.main()
