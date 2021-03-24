from tests.sample_pdus import *
import twseia
import pprint
import logging

FORMAT = '[%(levelname)s]: %(message)s'
logging.getLogger('').handlers = []
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


if __name__ == '__main__':
    # request = twseia.SAInfoRequestPacket.create(sa_info_type=twseia.SARegisterServiceIDEnum.REGISTRATION)
    # payload = request.to_pdu()
    # serial.write(payload)
    # kPANASONIC_FYTW_08810115_REGISTER_PDU = serial.read()
    # register = twseia.SARegisterPacket.from_pdu(pdu=kPANASONIC_FYTW_08810115_REGISTER_PDU)
    # print(f'{twseia.read_sa_cmd_helps(register=register)}')

    # pprint.pprint(twseia.AirConditioner.read_spec_cmd_helps())
    pass
