import unittest
import logging
import twseia
from tests.sample_pdus import *

FORMAT = '[%(levelname)s]: %(message)s'
logging.getLogger('').handlers = []
logging.basicConfig(level=logging.INFO, format=FORMAT)


class TestSmartApplication(unittest.TestCase):

    def test_create_register_cmd(self):
        register = twseia.create_read_register_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x00, 0xFF, 0xFF, 0x06])
        register = twseia.create_read_class_id_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x01, 0xFF, 0xFF, 0x07])
        register = twseia.create_read_protocol_version_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x02, 0xFF, 0xFF, 0x04])
        register = twseia.create_read_dev_type_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x04, 0xFF, 0xFF, 0x02])
        register = twseia.create_read_brand_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x05, 0xFF, 0xFF, 0x03])
        register = twseia.create_read_model_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x06, 0xFF, 0xFF, 0x00])
        register = twseia.create_read_supported_services_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x07, 0xFF, 0xFF, 0x01])
        register = twseia.create_current_states_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x08, 0xFF, 0xFF, 0x0E])

    def test_parsing_register_response(self):
        response = twseia.parsing_read_register_response(pdu=kPANASONIC_FYTW_08810115_REGISTER_PDU)
        self.assertTrue(isinstance(response, twseia.SAInfoRegisterPacket))
        assert isinstance(response, twseia.SAInfoRegisterPacket)
        logging.info(f'{response.to_json()}')
        self.assertTrue(response.type_id != 0x00)
        self.assertTrue(response.class_id < 4)
        self.assertTrue(response.service_id == 0x00)
        self.assertTrue(isinstance(response.brand, str))
        self.assertTrue(isinstance(response.model, str))
        self.assertTrue(isinstance(response.major_ver, int))
        self.assertTrue(isinstance(response.minor_ver, int))
        self.assertTrue(isinstance(response.services, list))
        self.assertTrue(len(response.services) > 0)

        # response = twseia.SmartApplication.parsing_read_class_id_response(pdu=)
        # assert isinstance(response, twseia.SAInfoRegisterPacket)
        # self.assertTrue(response.type_id == 0x00)
        # self.assertTrue(response.service_id == 0x01)
        # self.assertTrue(response.class_id < 4)
#
#         response = twseia.SmartApplication.parsing_read_version_response(pdu=test_pdu)
#         assert isinstance(response, twseia.SAInfoRegisterPacket)
#         self.assertTrue(response.type_id == 0x00)
#         self.assertTrue(response.service_id == 0x02)
#         self.assertTrue(isinstance(response.major_ver, int))
#         self.assertTrue(isinstance(response.minor_ver, int))
#
#         response = twseia.SmartApplication.parsing_read_dev_type_response(pdu=test_pdu)
#         assert isinstance(response, twseia.SAInfoRegisterPacket)
#         self.assertTrue(response.type_id == 0x00)
#         self.assertTrue(response.service_id == 0x04)
#
#         response = twseia.SmartApplication.parsing_read_brand_response(pdu=test_pdu)
#         assert isinstance(response, twseia.SAInfoRegisterPacket)
#         self.assertTrue(response.type_id == 0x00)
#         self.assertTrue(response.service_id == 0x05)
#         self.assertTrue(isinstance(response.brand, str))
#
#         response = twseia.SmartApplication.parsing_read_model_response(pdu=test_pdu)
#         assert isinstance(response, twseia.SAInfoRegisterPacket)
#         self.assertTrue(response.type_id == 0x00)
#         self.assertTrue(response.service_id == 0x06)
#         self.assertTrue(isinstance(response.model, str))
#
#         response = twseia.SmartApplication.parsing_read_services_response(pdu=test_pdu)
#         assert isinstance(response, twseia.SAInfoRegisterPacket)
#         self.assertTrue(response.type_id == 0x00)
#         self.assertTrue(response.service_id == 0x07)
#         self.assertTrue(isinstance(response.services, list))
#         self.assertTrue(len(response.services) > 0)
#
#         response = twseia.SmartApplication.parsing_read_all_states_response(pdu=test_pdu)
#         assert isinstance(response, twseia.SAInfoRegisterPacket)
#         self.assertTrue(response.type_id == 0x00)
#         self.assertTrue(response.service_id == 0x08)
#         self.assertTrue(isinstance(response.states, dict))
#         self.assertTrue(len(response.states) > 0)
#
#     def test_create_read_state_cmd(self):
#         pass
#
#     def test_parsing_read_state_response(self):
#         pass
#
#     def test_create_write_state_cmd(self):
#         pass
#
#     def test_parsing_write_state_response(self):
#         pass


class TestAirConditioner(unittest.TestCase):

    def test_interface_implementation(self):
        pdu = kHITACHI_AC_RAD_50NK_REGISTER_PDU
        packet = twseia.SAInfoRegisterPacket.from_pdu(pdu=pdu)
        self.assertTrue(isinstance(packet, twseia.SAInfoRegisterPacket))
        # pdu = kHITACHI_AC_RAS_50NF_REGISTER_PDU
        # packet = twseia.SAInfoRegisterPacket.from_pdu(pdu=pdu)
        # self.assertTrue(isinstance(packet, twseia.SAInfoRegisterPacket))


class TestDehumidifier(unittest.TestCase):
    def test_interface_implementation(self):
        pdu = kPANASONIC_FYTW_08810115_REGISTER_PDU
        packet = twseia.SAInfoRegisterPacket.from_pdu(pdu=pdu)
        self.assertTrue(isinstance(packet, twseia.SAInfoRegisterPacket))
