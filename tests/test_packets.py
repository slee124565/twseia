import sys
sys.path.append('.')
import unittest
from tests.sample_pdus import *
from twseia.constants import SARegisterServiceID
from twseia.packets import SAInfoRequestPacket
from twseia.packets import SAInfoRegisterPacket
# from twseia.constants import SADeviceType
# from twseia.constants import SAServiceIOMode


class TestPackets(unittest.TestCase):

    def test_sa_info_request_packet(self):
        pdu = [6, 0, 0, 255, 255, 6]  # Register Request Packet
        packet = SAInfoRequestPacket.create(sa_info_type=SARegisterServiceID.READ_ALL)
        self.assertEqual(packet.to_pdu(), pdu)

    def test_sa_info_register_packet(self):
        pdu = kHITACHI_AC_RAD_50NK_REGISTER_PDU
        packet = SAInfoRegisterPacket.from_pdu(pdu=pdu)
        self.assertTrue(packet)


if __name__ == '__main__':
    unittest.main()
