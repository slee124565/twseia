import unittest
import logging
import twseia
from tests.sample_pdus import *

FORMAT = '[%(levelname)s]: %(message)s'
logging.getLogger('').handlers = []
logging.basicConfig(level=logging.INFO, format=FORMAT)


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
