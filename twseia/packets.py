from .constants import SAServiceIOMode, SAClassID
from .constants import SADeviceType
from .constants import SARegisterServiceID
from .constants import SAPacketDataLenType
from .utils import compute_pdu_checksum
from .services import SADataValueType
from .devices import AirConditioner


class SARequestPacket:
    def to_pdu(self):
        raise NotImplementedError


class SAResponsePacket:
    @classmethod
    def from_pdu(cls, pdu: list):
        raise NotImplementedError


class _BasePacket:
    len = None
    type_id = None
    io_mode_id = None
    service_id = None
    data_type_id = None
    data_bytes = None
    checksum = None

    @classmethod
    def raise_if_packet_len_checksum_invalid(cls, pdu: list):
        if not isinstance(pdu, list):
            raise ValueError(f'pdu invalid, {pdu}')

        if pdu[0] != len(pdu):
            raise ValueError(f'pdu len check invalid, {pdu}')

        if pdu[-1] != compute_pdu_checksum(pdu=pdu[:-1]):
            raise ValueError(f'pdu checksum invalid, {pdu}')

    @classmethod
    def from_general_pdu(cls, pdu: list):
        cls.raise_if_packet_len_checksum_invalid(pdu=pdu)
        _pdu = list(pdu)
        packet = cls()
        packet.len = _pdu[0]
        packet.type_id = _pdu[1]
        packet.io_mode_id = _pdu[1] >> 7
        packet.service_id = _pdu[1] & 0x7F
        packet.data_bytes = _pdu[2:-1]
        packet.checksum = _pdu[-1]
        return packet

    @classmethod
    def from_data_type_pdu(cls, pdu: list):
        cls.raise_if_packet_len_checksum_invalid(pdu=pdu)
        _pdu = list(pdu)
        packet = cls()
        packet.len = _pdu[0]
        packet.type_id = _pdu[1]
        packet.io_mode_id = _pdu[1] >> 7
        packet.service_id = _pdu[1] & 0x7F
        packet.data_type_id = _pdu[2]
        packet.data_bytes = _pdu[3:-1]
        packet.checksum = _pdu[-1]
        return packet

    def to_general_pdu(self):
        pdu = [self.type_id, (self.io_mode_id << 7) | (self.service_id & 0x7F)] + self.data_bytes
        _len = len(pdu) + 2
        pdu.insert(0, _len)
        checksum = compute_pdu_checksum(pdu)
        pdu.append(checksum)
        return pdu

    def to_data_type_pdu(self):
        pdu = [self.type_id, (self.io_mode_id << 7) | (self.service_id & 0x7F), self.data_type_id] + self.data_bytes
        _len = len(pdu) + 2
        pdu.insert(0, len(pdu))
        checksum = compute_pdu_checksum(pdu)
        pdu.append(checksum)
        return pdu


class SAInfoRequestPacket(_BasePacket, SARequestPacket):
    """TAISEIA Spec. Graph_34"""

    @classmethod
    def from_pdu(cls, pdu: list):
        return super(SAInfoRequestPacket, cls).from_general_pdu(pdu=pdu)

    def to_pdu(self):
        return super(SAInfoRequestPacket, self).to_general_pdu()

    @classmethod
    def create(cls, sa_info_type: SARegisterServiceID = SARegisterServiceID.READ_ALL):
        packet = cls()
        packet.len = 6
        packet.type_id = 0x00
        packet.io_mode_id = SAServiceIOMode.READ.value
        packet.service_id = sa_info_type.value
        packet.data_bytes = [0xFF, 0xFF]
        return packet


class SAInfoDevStatesPacket(_BasePacket, SAResponsePacket):
    @classmethod
    def from_pdu(cls, pdu: list):
        pass


class SAInfoRegisterPacket(_BasePacket, SAResponsePacket):
    class_id = None
    major_ver = None  # protocol major version
    minor_ver = None  # protocol minor version
    fragment_offset = None  # fragment offset
    brand = None
    model = None
    services = []

    @classmethod
    def from_pdu(cls, pdu: list):
        cls.raise_if_packet_len_checksum_invalid(pdu=pdu)
        _pdu = list(pdu)
        packet = cls()
        packet.len = _pdu[0]
        assert _pdu[1] == 0x00
        packet.data_type_id = _pdu[2] >> 7  # PacketDataUnitType
        packet.class_id = _pdu[2] & 0x0F
        packet.major_ver = _pdu[3]
        packet.minor_ver = _pdu[4]
        packet.fragment_offset = _pdu[5]
        packet.type_id = SADeviceType(int.from_bytes(_pdu[6:8], 'big'))
        n_zero = _pdu[8:].index(0)
        packet.brand = bytearray(_pdu[8:8 + n_zero]).decode("utf-8")
        n_start = 8 + n_zero + 1
        n_zero = _pdu[n_start:].index(0)
        packet.model = bytearray(_pdu[n_start:n_start + n_zero]).decode("utf-8")
        n_start = n_start + n_zero + 1
        n = n_start
        packet.services = []
        is_fixed_len_pdu = True if packet.data_type_id == SAPacketDataLenType.FIXED_LEN else False
        while n < len(pdu)-1:
            if is_fixed_len_pdu:
                _len = 3
            else:
                data_type_id = _pdu[n + 1]
                _len = SADataValueType.read_data_type_len_by_id(data_type_id=data_type_id)

            service = AirConditioner.convert_dev_specific_service(
                pdu=pdu[n:n + _len],
                is_fixed_len_pdu=is_fixed_len_pdu
            )
            packet.services.append(service)
            n += _len
        return packet

    def to_json(self):
        return {
            'class_id': self.class_id,
            'class_name': SAClassID(self.class_id).name,
            'type_id': self.type_id,
            'type_name': SADeviceType(self.type_id).name,
            'version': (self.major_ver, self.minor_ver),
            'fragment_offset': self.fragment_offset,
            'brand': self.brand,
            'model': self.model,
            'services': [service.to_json() for service in self.services]
        }


class SAInfoResponsePacket(_BasePacket):
    """TAISEIA Spec. Graph_35"""

    @classmethod
    def from_pdu(cls, pdu: list):
        packet = super(SAInfoResponsePacket, cls).from_general_pdu(pdu=pdu)
        if packet.service_id == SARegisterServiceID.READ_ALL:
            if packet.io_mode_id != SAServiceIOMode.READ:
                raise ValueError(f'Packet io_mode_id {packet.io_mode_id} invalid')
            return SAInfoRegisterPacket.from_pdu(pdu=pdu)
        elif packet.service_id == SARegisterServiceID.READ_DEVICE_SERVICES_STATUS:
            return SAInfoDevStatesPacket.from_pdu(pdu=pdu)
        else:
            raise NotImplementedError


class SAStateReadRequestPacket(_BasePacket):
    """TAISEIA Spec. Graph_36"""

    @classmethod
    def create(cls, type_id: int, service_id: int):
        packet = cls()
        packet.len = 0x06
        packet.type_id = type_id
        packet.io_mode_id = SAServiceIOMode.READ.value
        packet.service_id = service_id
        packet.data_bytes = [0xFF, 0xFF]
        return packet

    def to_pdu(self):
        return self.to_general_pdu()


class SAStateReadResponsePacket(_BasePacket):
    """TAISEIA Spec. Graph_37"""

    @classmethod
    def from_pdu(cls, pdu: list):
        return cls.from_general_pdu(pdu=pdu)


class SAStateReadMultiRequestPacket:
    """TAISEIA Spec. Graph_38"""
    len = None
    type_id = None  # Table_10
    service_id = None  # Appendix, SA specific
    data_type_id = None
    data_bytes = None  # [0xFF] * N
    checksum = None


class SAStateReadMultiResponsePacket:
    """TAISEIA Spec. Graph_39"""
    len = None
    type_id = None  # Table_10
    service_id = None  # Appendix, SA specific
    data_type_id = None
    data_bytes = None
    checksum = None


class SASensorReadMultiRequestPacket:
    """TAISEIA Spec. Graph_40"""
    len = None
    type_id = None  # Table_10
    service_id = None  # Appendix, SA specific
    data_type_id = None
    data_bytes = None  # [0xFF] * N
    checksum = None


class SASensorReadMultiResponsePacket:
    """TAISEIA Spec. Graph_41"""
    len = None
    type_id = None  # Table_10
    service_id = None  # Appendix, SA specific
    data_type_id = None
    fragment_offset = None
    data_bytes = None
    checksum = None


class SAStateWriteRequestPacket(_BasePacket):
    """TAISEIA Spec. Graph_43"""

    @classmethod
    def create(cls, type_id: int, service_id: int, value: int):
        packet = cls()
        packet.len = 6
        packet.type_id = type_id
        packet.service_id = 0x80 & service_id
        packet.data_bytes = value.to_bytes(2, 'big')
        return packet

    def to_pdu(self):
        return self.to_general_pdu()


class SAStateWriteResponsePacket(SAStateWriteRequestPacket):

    @classmethod
    def from_pdu(cls, pdu: list):
        return cls.from_general_pdu(pdu=pdu)


class SAStateWriteMultiRequestPacket:
    """TAISEIA Spec. Graph_44"""
    len = None
    type_id = None  # Table_10
    service_id = None  # Appendix, SA specific
    data_type_id = None
    data_bytes = None  # [0xFF] * N
    checksum = None


__all__ = [
    'SAInfoRequestPacket',
    'SAInfoResponsePacket',
    'SAStateReadRequestPacket',
    'SAInfoRegisterPacket',
    'SAInfoDevStatesPacket',
    'SAStateReadResponsePacket',
    'SAStateWriteRequestPacket',
    'SAStateWriteResponsePacket',
    'SASensorReadMultiResponsePacket',
]
