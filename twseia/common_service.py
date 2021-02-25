import enum
from .constants import SAServiceID


class ServiceIOMode(enum.IntEnum):
    READ = 0x00
    READ_WRITE = 0x01


class CommonService:
    io_mode = None
    service_type = None
    high_byte_value = None
    low_byte_value = None

    @property
    def value(self):
        return int.from_bytes(bytes([self.high_byte_value, self.low_byte_value]), 'big')

    @classmethod
    def from_pdu(cls, pdu: list):
        if not isinstance(pdu, list) or len(pdu) != 4:
            raise ValueError(f'pdu type invalid, {pdu}')
        service = CommonService()
        service.io_mode = ServiceIOMode(pdu[0] >> 7)
        service.service_type = SAServiceID(pdu[0] & 0x7F)
        service.high_byte_value = pdu[1]
        service.low_byte_value = pdu[2]

    def to_pdu(self):
        return [
            self.io_mode << 7 | self.service_type & 0x7F,
            self.high_byte_value,
            self.low_byte_value
        ]

    def to_json(self):
        return {
            'io_mode': self.io_mode,
            'service_type': self.service_type,
            'high_byte_value': self.high_byte_value,
            'low_byte_value': self.low_byte_value,
            'value': self.value
        }
