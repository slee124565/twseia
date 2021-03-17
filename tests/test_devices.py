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
        register = twseia.create_read_all_states_cmd()
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
        # self.assertTrue(class_id in [n.value for n in list(twseia.SAClassID)])
        self.assertEqual(class_id, 0)
        logging.debug(f'class_id {class_id}')

    def test_parsing_sa_protocol_version_response(self):
        version = twseia.parsing_sa_protocol_version_response(pdu=kPANASONIC_FYTW_08810115_READ_VERSION_PDU)
        self.assertTrue(isinstance(version, tuple))
        self.assertTrue(len(version) == 2)
        self.assertEqual(version[0], 4)
        self.assertEqual(version[1], 0)
        logging.debug(f'version {version}')

    def test_parsing_sa_dev_type_response(self):
        type_id = twseia.parsing_sa_dev_type_response(pdu=kPANASONIC_FYTW_08810115_READ_DEV_TYPE_PDU)
        assert isinstance(type_id, int)
        # self.assertTrue(type_id in [n.value for n in list(twseia.SATypeIDEnum)])
        self.assertEqual(type_id, 4)
        logging.debug(f'type_id {type_id}')

    def test_parsing_sa_brand_response(self):
        brand = twseia.parsing_sa_brand_response(pdu=kPANASONIC_FYTW_08810115_READ_BRAND_PDU)
        self.assertTrue(isinstance(brand, str))
        self.assertEqual(brand, 'Panasonic')
        logging.debug(f'brand {brand}')

    def test_parsing_sa_model_response(self):
        model = twseia.parsing_sa_model_response(pdu=kPANASONIC_FYTW_08810115_READ_MODEL_PDU)
        self.assertTrue(isinstance(model, str))
        self.assertEqual(model, 'FYTW-05760121')
        logging.debug(f'model {model}')

    def test_parsing_dehumidifier_services_response(self):
        services = twseia.parsing_dehumidifier_services_response(
            pdu=kPANASONIC_FYTW_08810115_SERVICES_PDU,
            is_fixed_len_pdu=True
        )
        self.assertTrue(isinstance(services, list), f'services type {type(services)}')
        for service in services:
            self.assertTrue(isinstance(service, dict), f'service type {type(service)}')
            self.assertTrue(service.get('txt') is not None)
            self.assertTrue(service.get('mode') is not None)
            self.assertTrue(service.get('type') is not None)
            if service.get('mode') == 'RW':
                self.assertTrue(service.get('params') is not None, f'{service}')
            if service.get('unit'):
                self.assertTrue(service.get('unit') is not None)
            logging.debug(f'service: {service}')

    def test_parsing_dehumidifier_all_states_response(self):
        states = twseia.parsing_dehumidifier_all_states_response(
            pdu=kPANASONIC_FYTW_08810115_ALL_STATES_PDU,
            is_fixed_len_pdu=True
        )
        self.assertTrue(isinstance(states, list))
        for state in states:
            self.assertTrue(isinstance(state, dict))
            self.assertTrue(state.get('name') is not None)
            self.assertTrue(state.get('value') is not None)
            logging.debug(f'state: {state}')

    def test_parsing_air_conditioner_services_response(self):
        # todo
        pass

    def test_parsing_air_conditioner_states_response(self):
        # todo
        pass

    def test_create_read_state_cmd(self):
        register = twseia.SARegisterPacket.from_pdu(pdu=kPANASONIC_FYTW_08810115_REGISTER_PDU)
        for service in register.services:
            self.assertTrue(isinstance(service, twseia.SAServiceBase))
            assert isinstance(service, twseia.SAServiceBase)
            cmd = twseia.create_read_state_cmd(
                type_id=register.type_id,
                service_id=service.service_id
            )
            self.assertTrue(isinstance(cmd, list))
            self.assertTrue(len(cmd) == 6 and cmd[0] == 6)
            self.assertEqual(cmd[1], register.type_id)
            self.assertEqual(cmd[2], service.service_id & 0x7F)
            self.assertEqual(cmd[3], 0xFF)
            self.assertEqual(cmd[4], 0xFF)
            self.assertEqual(cmd[-1], twseia.compute_pdu_checksum(cmd[:-1]))
            logging.debug(f'read_state_cmd: {cmd}')

    # def test_parsing_read_state_response(self):
    #     pass

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
