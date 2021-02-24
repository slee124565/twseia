class CommonPacket:
    _pdu = None
    len = None
    sa_type_id = None
    cmd_type_id = None
    service_id = None
    high_byte_value = None
    low_byte_value = None
    check_sum = None

    @classmethod
    def compute_checksum(cls, pdu: list):
        _checksum = 0
        for x in pdu:
            _checksum ^= x
        return _checksum

    @classmethod
    def from_pdu(cls, pdu: list):
        if not isinstance(pdu, list):
            raise ValueError(f'pdu not list, {pdu}')
        if pdu[0] != len(pdu) or len(pdu) != 6:
            raise ValueError(f'pdu len invalid, {pdu}')
        if pdu[-1] != cls.compute_checksum(pdu=pdu[:-1]):
            raise ValueError(f'pdu checksum invalid, {pdu}')

        _packet = cls()
        _packet._pdu = pdu
        _packet.len = pdu[0]
        _packet.sa_type_id = pdu[1]
        _packet.cmd_type_id = pdu[2] >> 7
        _packet.service_id = pdu[2] & 0x7f
        _packet.high_byte_value = pdu[3]
        _packet.low_byte_value = pdu[4]
        _packet.check_sum = pdu[5]
        return _packet

    def to_pdu(self):
        # if isinstance(self.len, int) and isinstance(self.sa_type_id, int)
        _pdu = [self.len, self.sa_type_id, (self.cmd_type_id << 7) | self.service_id, self.high_byte_value,
                self.low_byte_value]
        return _pdu.append(self.compute_checksum(_pdu))
