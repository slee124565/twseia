import unittest
from twseia.packets import CommonPacket
from twseia.constants import SADeviceType
from twseia.constants import SACmdType
from twseia.constants import SAServiceID


class TestCommonPackets(unittest.TestCase):

    def test_convert_pdu(self):
        pdu = [6, 0, 0, 255, 255, 6]  # Register Request Packet
        packet = CommonPacket.from_pdu(pdu=pdu)
        self.assertEqual(packet.to_pdu(), pdu)
        self.assertTrue(isinstance(packet.to_json(), dict))
        self.assertEqual(packet.len, pdu[0])
        self.assertEqual(packet.sa_type_id, pdu[1])
        self.assertEqual(packet.cmd_type_id, pdu[2] >> 7)
        self.assertEqual(packet.service_id, pdu[2] & 0x7F)
        self.assertEqual(packet.high_byte_value, pdu[3])
        self.assertEqual(packet.low_byte_value, pdu[4])
        self.assertEqual(packet.check_sum, pdu[5])

    def test_create_pdu(self):
        packet = CommonPacket.create_packet(
            sa_dev_type=SADeviceType.REGISTER,
            cmd_type=SACmdType.READ,
            sa_service=SAServiceID.REGISTER,
            value=0xFFFF
        )
        self.assertEqual(packet.to_pdu(), [6, 0, 0, 255, 255, 6])

        packet = CommonPacket.create_packet(
            sa_dev_type=SADeviceType.REGISTER,
            cmd_type=SACmdType.READ,
            sa_service=SAServiceID.REGISTER
        )
        self.assertEqual(packet.to_pdu(), [6, 0, 0, 255, 255, 6])
