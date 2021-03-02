import enum


class SADataValueType(enum.IntEnum):
    ENUM16 = 0x01
    ENUM16_BIT = 0x06

    UNIT8 = 0x0a
    UNIT16 = 0x0b
    UINT32 = 0x0c
    UINT64 = 0x0d

    INT8 = 0x0f
    INT16 = 0x10
    INT32 = 0x11

    TIME_MD = 0x14
    TIME_HM = 0x15
    TIME_MS = 0x16
    TIME_YMDHMS = 0x17
    TIME_YMDHM = 0x18

    STR = 0x20


class ServiceBase:
    io_mode_id = None
    service_id = None
    data_type_id = None
    data_bytes = None

    @classmethod
    def from_fixed_len_pdu(cls, pdu: list):
        if not isinstance(pdu, list):
            raise ValueError(f'pdu type invalid, {pdu}')
        if len(pdu) != 3:
            raise ValueError(f'pdu len invalid, {pdu}')
        _pdu = list(pdu)
        service = cls()
        service.io_mode_id = _pdu[0] >> 7
        service.service_id = _pdu[0] & 0x7F
        service.data_bytes = _pdu[1:]
        return service

    @classmethod
    def from_dynamic_len_pdu(cls, pdu: list):
        if not isinstance(pdu, list):
            raise ValueError(f'pdu type invalid, {pdu}')
        if len(pdu) >= 3:
            raise ValueError(f'pdu len invalid, {pdu}')
        _pdu = list(pdu)
        service = cls()
        service.io_mode_id = _pdu[0] >> 7
        service.service_id = _pdu[0] & 0x7F
        service.data_type_id = _pdu[1]
        service.data_bytes = _pdu[2:]
        return service


class SAService:
    @classmethod
    def from_service(cls, service: ServiceBase) -> ServiceBase:
        raise NotImplementedError


class Enum16Service(ServiceBase, SAService):
    ID = 0x01

    @classmethod
    def from_service(cls, service: ServiceBase) -> ServiceBase:
        type_service = cls()
        type_service.io_mode_id = service.io_mode_id
        type_service.service_id = service.service_id
        type_service.data_type_id = service.data_type_id
        type_service.data_bytes = list(service.data_bytes)
        return type_service

    def read_value(self):
        return int.from_bytes(self.data_bytes[-2:], 'big')


class Enum16BitService(ServiceBase):
    ID = 0x06

    def read_bit(self, bit_index: int) -> int:
        assert (bit_index <= 15) and (bit_index >= 0)
        if 0 <= bit_index <= 7:
            mask = 1 << bit_index
            return (self.data_bytes[0] & mask) >> bit_index
        elif 8 <= bit_index <= 15:
            mask = 1 << (bit_index-8)
            return (self.data_bytes[1] & mask) >> (bit_index-8)


class UInt8Service(ServiceBase):
    ID = 0x0A

    @property
    def max(self):
        raise NotImplementedError

    @property
    def min(self):
        raise NotImplementedError


class UInt16ServiceInfo(ServiceBase):
    CODE = 0x0B

    @property
    def max(self):
        raise NotImplementedError


def query_data_type_bytes_len(data_type_id: int):
    if data_type_id in [0x01, 0x06, 0x0A, 0x0F, 0x14, 0x15, 0x16]:
        return 2
    elif data_type_id in [0x0B, 0x010]:
        return 4
    elif data_type_id in [0x18]:
        return 5
    elif data_type_id in [0x17]:
        return 6
    elif data_type_id in [0x0C, 0x11]:
        return 8
    elif data_type_id in [0x0D]:
        return 16
    else:
        raise ValueError(f'data_type_id invalid, {data_type_id}')


class ServiceInfoFactory:
    @classmethod
    def convert_to_general_service_info(cls, pdu: list):
        if not isinstance(pdu, list):
            raise ValueError
        if len(pdu) != 3:
            raise ValueError
        # io_mode_id = pdu[0] >> 7
        # service_id = pdu[0] & 0x7F
        # # data_bytes = pdu[1:]
        # if service_id == SADataValueType.ENUM16:
        #     return Enum16ServiceInfo.from_general_pdu(pdu=pdu)
        # elif service_id == SADataValueType.ENUM16_BIT:
        #     return Enum16BitServiceInfo.from_general_pdu(pdu=pdu)
        return None

    @classmethod
    def convert_to_data_type_service_(cls, pdu: list):
        raise NotImplementedError


class SABasicServiceFactory:
    @classmethod
    def convert_basic_service_from_pdu(cls, pdu: list, is_fixed_len_pdu: True):
        if is_fixed_len_pdu:
            return ServiceBase.from_fixed_len_pdu(pdu=pdu)
        else:
            return ServiceBase.from_dynamic_len_pdu(pdu=pdu)


__all__ = [
    'SABasicServiceFactory',
    'ServiceBase',
    'Enum16Service',
    'Enum16BitService',
    'UInt8Service',
]
