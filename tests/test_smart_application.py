import unittest
import logging
import twseia

FORMAT = '[%(levelname)s]: %(message)s'
logging.getLogger('').handlers = []
logging.basicConfig(level=logging.INFO, format=FORMAT)


class TestSmartApplication(unittest.TestCase):

    def setUp(self) -> None:
        self.sa = twseia.SmartApplication()
        self.sa.register()
        self.assertTrue(isinstance(self.sa.device, twseia.SAInfoRegisterPacket))

    def test_read_service(self):
        for service in self.sa.device.services:
            assert isinstance(service, twseia.SAServiceBase)
            response = self.sa.read_state(
                service_id=service.service_id)
            logging.debug(f'{response.to_json()}')
            self.assertTrue(isinstance(response, twseia.SAStateReadResponsePacket))
            self.assertEqual(response.service_id, service.service_id)

    # def test_write_service(self):
    #     raise NotImplementedError


if __name__ == '__main__':
    unittest.main()
