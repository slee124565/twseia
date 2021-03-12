from tests.sample_pdus import *
import twseia

if __name__ == '__main__':
    register = twseia.SAInfoRegisterPacket.from_pdu(pdu=kPANASONIC_FYTW_08810115_REGISTER_PDU)
    print(f'{twseia.read_sa_cmd_helps(register=register)}')
