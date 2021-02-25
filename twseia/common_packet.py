from .constants import SACmdType
from .constants import SADeviceType
from .constants import SAServiceID
from .utils import compute_pdu_checksum


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
    def create_packet(cls, sa_dev_type: SADeviceType, cmd_type: SACmdType, sa_service: SAServiceID,
                      value: int = 0xFFFF):
        _packet = cls()
        _packet.len = 6
        _packet.sa_type_id = sa_dev_type.value
        _packet.cmd_type_id = cmd_type.value
        _packet.service_id = sa_service.value
        _bytes = value.to_bytes(2, 'big')
        _packet.high_byte_value = _bytes[0]
        _packet.low_byte_value = _bytes[1]
        return _packet

    @classmethod
    def from_pdu(cls, pdu: list):
        if not isinstance(pdu, list):
            raise ValueError(f'pdu not list, {pdu}')
        if pdu[0] != len(pdu) or len(pdu) != 6:
            raise ValueError(f'pdu len invalid, {pdu}')
        if pdu[-1] != compute_pdu_checksum(pdu=pdu[:-1]):
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

    def to_json(self):
        return {
            'len': self.len,
            'sa_type_id': self.sa_type_id,
            'cmd_type_id': self.cmd_type_id,
            'service_id': self.service_id,
            'high_byte_value': self.high_byte_value,
            'low_byte_value': self.low_byte_value
        }

    def to_pdu(self):
        if not isinstance(self.len, int) or self.cmd_type_id not in [e.value for e in SACmdType] \
                or not isinstance(self.service_id, int) or not isinstance(self.high_byte_value, int) \
                or not isinstance(self.low_byte_value, int):
            raise ValueError(f'{self.to_json()}')
        self._pdu = [
            self.len,
            self.sa_type_id,
            (self.cmd_type_id << 7) | self.service_id,
            self.high_byte_value,
            self.low_byte_value
        ]
        self._pdu.append(compute_pdu_checksum(self._pdu))
        return self._pdu


__all__ = ['CommonPacket']
