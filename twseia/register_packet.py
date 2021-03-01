from .utils import compute_pdu_checksum
from .constants import SAClassID
from .constants import SADeviceType
from .constants import SAPacketDataLenType
from .constants import SARegisterServiceID


class GeneralServiceUnit:
    rw_mode_id = None
    service_id = None
    data_bytes = None

    @classmethod
    def from_pdu(cls, pdu: list):
        service = cls()
        _pdu = list(pdu)
        service.rw_mode_id = _pdu[0] >> 7
        service.service_id = _pdu[0] & 0x7F
        service.data_bytes = _pdu[1:]


class MultiByteServiceUnit(GeneralServiceUnit):
    data_type_id = None

    @classmethod
    def from_pdu(cls, pdu: list):
        _pdu = list(pdu)
        service = super(MultiByteServiceUnit, cls).from_pdu(pdu=_pdu)
        service.data_type_id = _pdu[1]
        service.data_bytes = _pdu[2:]
        return service


class _RegisterPacket:
    _pdu = None
    len = None
    service_data_type = None
    sa_class = None
    major_ver = None  # protocol major version
    minor_ver = None  # protocol minor version
    fragment_offset = None  # fragment offset
    sa_type = None
    brand = None
    model = None
    services = []
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
        if pdu[1] != SARegisterServiceID.READ_ALL:
            raise ValueError(f'pdu[1] value should be fixed 0x00, {pdu[1]}')
        packet.service_data_type = SAServiceDataType(pdu[2] >> 7)
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
        if packet.service_data_type == SAPacketDataLenType.FIXED_LEN:
            pass
        else:  # SAServiceUnitType.MULTI_BYTE
            pass
        return packet
