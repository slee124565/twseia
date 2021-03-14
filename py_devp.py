from tests.sample_pdus import *
import twseia

if __name__ == '__main__':
    request = twseia.SAInfoRequestPacket.create(sa_info_type=twseia.SARegisterServiceIDEnum.REGISTRATION)
    payload = request.to_pdu()
    # serial.write(payload)
    # kPANASONIC_FYTW_08810115_REGISTER_PDU = serial.read()
    register = twseia.SAInfoRegisterPacket.from_pdu(pdu=kPANASONIC_FYTW_08810115_REGISTER_PDU)
    print(f'{twseia.read_sa_cmd_helps(register=register)}')
