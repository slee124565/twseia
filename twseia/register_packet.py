class RegisterPacket:

    @classmethod
    def from_pdu(cls, pdu: list):
        if not isinstance(pdu, list):
            raise ValueError(f'{pdu}')

