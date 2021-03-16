import unittest
import logging
import twseia
from tests.sample_pdus import *

FORMAT = '[%(levelname)s]: %(message)s'
logging.getLogger('').handlers = []
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


class TestSmartApplication(unittest.TestCase):

    def test_create_register_cmd(self):
        register = twseia.create_sa_register_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x00, 0xFF, 0xFF, 0x06])
        register = twseia.create_sa_class_id_cmd()
        self.assertEqual(register, [0x06, 0x00, 0x01, 0xFF, 0xFF, 0x07])
        register = twseia.create_sa_protocol_version_cmd()
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

    def test_parsing_sa_register_response(self):
        responses = [
            kPANASONIC_FYTW_08810115_REGISTER_PDU,
            kHITACHI_AC_RAD_50NK_REGISTER_PDU,
            # kHITACHI_AC_RAS_50NF_REGISTER_PDU
        ]
        for response in responses:
            packet = twseia.parsing_sa_register_response(pdu=response)
            self.assertTrue(isinstance(packet, twseia.SARegisterPacket))
            assert isinstance(packet, twseia.SARegisterPacket)
            logging.info(f'{packet.to_json()}')
            self.assertTrue(packet.type_id != 0x00)
            self.assertTrue(packet.class_id < 4)
            self.assertTrue(isinstance(packet.brand, str))
            self.assertTrue(isinstance(packet.model, str))
            self.assertTrue(isinstance(packet.major_ver, int))
            self.assertTrue(isinstance(packet.minor_ver, int))
            self.assertTrue(isinstance(packet.services, list))
            self.assertTrue(len(packet.services) > 0)

    def test_parsing_sa_class_id_response(self):
        class_id = twseia.parsing_sa_class_id_response(pdu=kPANASONIC_FYTW_08810115_READ_CLASS_ID_PDU)
        self.assertTrue(class_id in [n.value for n in list(twseia.SAClassID)])
        logging.debug(f'class_id {class_id}')

    def test_parsing_sa_protocol_version_response(self):
        version = twseia.parsing_sa_protocol_version_response(pdu=kPANASONIC_FYTW_08810115_READ_VERSION_PDU)
        self.assertTrue(isinstance(version, tuple))
        self.assertTrue(len(version) == 2)
        logging.debug(f'version {version}')

    def test_parsing_sa_dev_type_response(self):
        type_id = twseia.parsing_sa_dev_type_response(pdu=kPANASONIC_FYTW_08810115_READ_DEV_TYPE_PDU)
        assert isinstance(type_id, int)
        self.assertTrue(type_id in [n.value for n in list(twseia.SATypeIDEnum)])
        logging.debug(f'type_id {type_id}')

    def test_parsing_sa_brand_response(self):
        brand = twseia.parsing_sa_brand_response(pdu=kPANASONIC_FYTW_08810115_READ_BRAND_PDU)
        self.assertTrue(isinstance(brand, str))
        logging.debug(f'brand {brand}')

    def test_parsing_sa_model_response(self):
        model = twseia.parsing_sa_model_response(pdu=kPANASONIC_FYTW_08810115_READ_MODEL_PDU)
        self.assertTrue(isinstance(model, str))
        logging.debug(f'model {model}')

    # def test_parsing_dehumidifier_services_response(self):
    #     services = twseia.Dehumidifier.parsing_sa_services_response(pdu=kPANASONIC_FYTW_08810115_SERVICES_PDU)
    #     self.assertTrue(isinstance(services, list))
    #
    # def test_parsing_dehumidifier_all_states_response(self):
    #     states = twseia.Dehumidifier.parsing_sa_all_states_response(pdu=kPANASONIC_FYTW_08810115_ALL_STATES_PDU)
    #     self.assertTrue(isinstance(states, list))

    # def test_create_read_state_cmd(self):
    #     pass
    #
    # def test_parsing_read_state_response(self):
    #     pass
    #
    # def test_create_write_state_cmd(self):
    #     pass
    #
    # def test_parsing_write_state_response(self):
    #     pass


class TestAirConditioner(unittest.TestCase):

    def test_interface_implementation(self):
        pdu = kHITACHI_AC_RAD_50NK_REGISTER_PDU
        packet = twseia.SARegisterPacket.from_pdu(pdu=pdu)
        self.assertTrue(isinstance(packet, twseia.SARegisterPacket))
        # pdu = kHITACHI_AC_RAS_50NF_REGISTER_PDU
        # packet = twseia.SAInfoRegisterPacket.from_pdu(pdu=pdu)
        # self.assertTrue(isinstance(packet, twseia.SAInfoRegisterPacket))


class TestDehumidifier(unittest.TestCase):
    def test_interface_implementation(self):
        pdu = kPANASONIC_FYTW_08810115_REGISTER_PDU
        packet = twseia.SARegisterPacket.from_pdu(pdu=pdu)
        self.assertTrue(isinstance(packet, twseia.SARegisterPacket))


if __name__ == '__main__':
    unittest.main()
