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

    @classmethod
    def read_data_type_len_by_id(cls, data_type_id: int) -> int:
        if data_type_id == cls.ENUM16:
            return 2
        else:
            raise NotImplementedError

    @classmethod
    def query_data_type_bytes_len(cls, data_type_id: int):
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

    def read_value(self):
        return int.from_bytes(self.data_bytes[-1:], 'big')

    def read_max(self):
        return int.from_bytes(self.data_bytes[-2:-1], 'big')

    def read_min(self):
        return int.from_bytes(self.data_bytes[-1:], 'big')


class UInt16Service(ServiceBase):
    ID = 0x0B

    def read_value(self):
        return int.from_bytes(self.data_bytes[-2:], 'big')

    def read_max(self):
        return int.from_bytes(self.data_bytes[-4:-2], 'big')

    def read_min(self):
        return int.from_bytes(self.data_bytes[-2:], 'big')


class UInt32Service(ServiceBase):
    ID = 0x0C

    def read_value(self):
        return int.from_bytes(self.data_bytes[-4:], 'big')

    def read_max(self):
        return int.from_bytes(self.data_bytes[-8:-4], 'big')

    def read_min(self):
        return int.from_bytes(self.data_bytes[-4:], 'big')


class UInt64Service(ServiceBase):
    ID = 0x0D

    def read_value(self):
        return int.from_bytes(self.data_bytes[-8:], 'big')

    def read_max(self):
        return int.from_bytes(self.data_bytes[-16:-8], 'big')

    def read_min(self):
        return int.from_bytes(self.data_bytes[-8:], 'big')


class Int8Service(ServiceBase):
    ID = 0x0F

    def read_value(self):
        return int.from_bytes(self.data_bytes[-1:], 'big', signed=True)

    def read_max(self):
        return int.from_bytes(self.data_bytes[-2:-1], 'big', signed=True)

    def read_min(self):
        return int.from_bytes(self.data_bytes[-1:], 'big', signed=True)


class Int16Service(ServiceBase):
    ID = 0x10

    def read_value(self):
        return int.from_bytes(self.data_bytes[-2:], 'big', signed=True)

    def read_max(self):
        return int.from_bytes(self.data_bytes[-4:-2], 'big', signed=True)

    def read_min(self):
        return int.from_bytes(self.data_bytes[-2:], 'big', signed=True)


class Int32Service(ServiceBase):
    ID = 0x11

    def read_value(self):
        return int.from_bytes(self.data_bytes[-4:], 'big', signed=True)

    def read_max(self):
        return int.from_bytes(self.data_bytes[-4:-2], 'big', signed=True)

    def read_min(self):
        return int.from_bytes(self.data_bytes[-2:], 'big', signed=True)


class MDService(ServiceBase):
    ID = 0x14

    def read_value(self):
        return (int.from_bytes(self.data_bytes[-2:1], 'big'),
                int.from_bytes(self.data_bytes[-1:], 'big'))

    def read_month(self):
        return self.read_value()[0]

    def read_day(self):
        return self.read_value()[1]


class HMService(ServiceBase):
    ID = 0x15

    def read_value(self):
        return (int.from_bytes(self.data_bytes[-2:1], 'big'),
                int.from_bytes(self.data_bytes[-1:], 'big'))

    def read_hour(self):
        return self.read_value()[0]

    def read_minute(self):
        return self.read_value()[1]


class MSService(ServiceBase):
    ID = 0x16

    def read_value(self):
        return (int.from_bytes(self.data_bytes[-2:1], 'big'),
                int.from_bytes(self.data_bytes[-1:], 'big'))

    def read_minute(self):
        return self.read_value()[0]

    def read_second(self):
        return self.read_value()[1]


class YMDHMSService(ServiceBase):
    ID = 0x17
    pass


class YMDHMService(ServiceBase):
    ID = 0x18
    pass


class StringService(ServiceBase):
    ID = 0x20
    pass


__all__ = [
    'SADataValueType',
    'ServiceBase',
    'Enum16Service',
    'Enum16BitService',
    'UInt8Service',
    'UInt16Service',
    'UInt32Service',
    'UInt64Service',
    'Int8Service',
    'Int16Service',
    'Int32Service',
    'MDService',
    'HMService',
    'MSService'
]
