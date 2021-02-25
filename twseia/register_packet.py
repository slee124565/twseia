import enum
from .constants import SAClassID
from .constants import SADeviceType
from .utils import compute_pdu_checksum


class RegisterPacketType(enum.IntEnum):
    GENERAL = 0
    MULTIPLE = 1


class RegisterPacket:
    _pdu = None
    len = None
    packet_type = None
    sa_class = None
    major_ver = None  # protocol major version
    minor_ver = None  # protocol minor version
    fragment_offset = None  # fragment offset
    sa_type = None
    brand = None
    model = None
    services = {}
    check_sum = None

    @classmethod
    def from_pdu(cls, pdu: list):
        if not isinstance(pdu, list):
            raise ValueError(f'pdu not list, {pdu}')
        if pdu[0] != len(pdu):
            raise ValueError(f'pdu len invalid, {pdu}')
        if pdu[-1] != compute_pdu_checksum(pdu=pdu[:-1]):
            raise ValueError(f'pdu checksum invalid, {pdu}')
        packet = cls()
        packet._pdu = pdu
        packet.len = pdu[0]
        if pdu[1] != 0x00:
            raise ValueError(f'pdu[1] value should be fixed 0x00, {pdu[1]}')
        packet.packet_type = RegisterPacketType(pdu[2] >> 7)
        packet.dev_class = SAClassID(pdu[2] & 0x0f)
        packet.major_ver = pdu[3]
        packet.minor_ver = pdu[4]
        packet.fragment_offset = pdu[5]
        packet.sa_type = SADeviceType(int.from_bytes(pdu[6:8], 'big'))
        n_zero = pdu[8:].index(0)
        packet.brand = bytearray(pdu[8:8+n_zero]).decode("utf-8")
        n_start = 8 + n_zero + 1
        n_zero = pdu[n_start:].index(0)
        packet.model = bytearray(pdu[n_start:n_start+n_zero]).decode("utf-8")
        n_start = n_start+n_zero+1

