import unittest
from tests.sample_pdus import *
import twseia


class TestSAInfoRegisterPackets(unittest.TestCase):

    def test_sa_info_request_packet(self):
        pdu = [6, 0, 0, 255, 255, 6]  # Register Request Packet
        packet = twseia.SAInfoRequestPacket.create(
            sa_info_type=twseia.SARegisterServiceIDEnum.REGISTRATION
        )
        self.assertEqual(packet.to_pdu(), pdu)

    def test_sa_info_register_packet(self):
        pdu = kHITACHI_AC_RAD_50NK_REGISTER_PDU
        packet = twseia.SARegisterPacket.from_pdu(pdu=pdu)
        self.assertEqual(packet.type_id, twseia.SATypeIDEnum.AIR_CONDITIONER)
        self.assertEqual(packet.class_id, twseia.SAClassID.HOME_DEVICE)
        self.assertEqual(packet.data_type_id, twseia.SAPacketDataLenType.FIXED_LEN)
        self.assertEqual(packet.major_ver, 4)
        self.assertEqual(packet.minor_ver, 0)
        self.assertEqual(packet.brand, 'HITACHI')
        self.assertEqual(packet.model, 'RAD-50NK')
        self.assertEqual(len(packet.services), 18)
        for service in packet.services:
            self.assertTrue(isinstance(service, twseia.SAServiceBase))
            self.assertTrue(twseia.ACServiceIDEnum(service.service_id).name,
                            f'service_id {service.service_id}')
        self.assertTrue(packet)


if __name__ == '__main__':
    unittest.main()
