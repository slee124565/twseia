import enum


class SADataValueType(enum.IntEnum):
    ENUM16 = 0x01
    ENUM16_BIT = 0x06

    UNIT8 = 0x0a
    UINT16 = 0x0b
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


class SACmdHelp:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @property
    def id(self):
        return self.kwargs.get('id')

    @property
    def txt(self):
        return self.kwargs.get('txt', None)

    @property
    def mode(self):
        return self.kwargs.get('mode', None)

    @property
    def value_type(self):
        return self.kwargs.get('type', None)

    @property
    def params(self):
        return self.kwargs.get('params')

    @property
    def unit(self):
        return self.kwargs.get('unit')

    def update_kwargs(self, name, value):
        self.kwargs.update({
            name: value
        })

    def update_kwargs_type(self, value):
        self.kwargs.update({
            'type': value
        })

    def update_kwargs_params(self, value):
        self.kwargs.update({
            'params': value
        })

    def update_kwargs_unit(self, value):
        self.kwargs.update({
            'unit': value
        })

    def to_json(self):
        response = {
            'id': self.id,
            'txt': self.txt,
            'mode': self.mode,
            'type': self.value_type,
            'params': self.params,
        }
        if self.unit:
            response['unit'] = self.unit
        return response

    def __str__(self):
        return '{}'.format(self.to_json())


class SAServiceBase:
    io_mode_id = None
    service_id = None
    data_type_id = None
    data_bytes = None
    name = None

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
        service.name = cls.__doc__

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

    def to_json(self):
        return {
            'io_mode_id': self.io_mode_id,
            'service_id': self.service_id,
            'data_bytes': self.data_bytes,
            'name': self.name
        }

    def to_cmd_help(self) -> SACmdHelp:
        arr = self.name.split('_')
        txt = '_'.join([str(n).lower() for n in arr[:-1]])
        kwargs = {
            'id': self.service_id,
            'class': f'{self.__class__.__name__}',
            'txt': txt,
            'mode': 'RW' if self.io_mode_id == 1 else 'R',
            'type': f'{self.__class__.__name__.replace("Service", "")}',
            # 'bytes': self.data_bytes
        }
        return SACmdHelp(**kwargs)

    def read_value(self):
        return self.data_bytes

    def to_state_report(self):
        return {
            'name': self.name,
            'value': self.read_value(),
        }


class Enum16Service(SAServiceBase):
    ID = 0x01

    def read_value(self):
        return int.from_bytes(self.data_bytes[-2:], 'big')

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(Enum16Service, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help


class Enum16BitService(SAServiceBase):
    ID = 0x06

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(Enum16BitService, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help

    def read_bit(self, bit_index: int) -> int:
        assert (bit_index <= 15) and (bit_index >= 0)
        if 0 <= bit_index <= 7:
            mask = 1 << bit_index
            return (self.data_bytes[0] & mask) >> bit_index
        elif 8 <= bit_index <= 15:
            mask = 1 << (bit_index - 8)
            return (self.data_bytes[1] & mask) >> (bit_index - 8)

    def read_value(self):
        return '0b{:016b}'.format(int.from_bytes(self.data_bytes, 'big'))


class UInt8Service(SAServiceBase):
    ID = 0x0A

    def read_value(self):
        return int.from_bytes(self.data_bytes[-1:], 'big')

    def read_max(self):
        return int.from_bytes(self.data_bytes[-2:-1], 'big')

    def read_min(self):
        return int.from_bytes(self.data_bytes[-1:], 'big')

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(UInt8Service, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help


class UInt16Service(SAServiceBase):
    ID = 0x0B

    def read_value(self):
        return int.from_bytes(self.data_bytes[-2:], 'big')

    def read_max(self):
        return int.from_bytes(self.data_bytes[-4:-2], 'big')

    def read_min(self):
        return int.from_bytes(self.data_bytes[-2:], 'big')

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(UInt16Service, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help


class UInt32Service(SAServiceBase):
    ID = 0x0C

    def read_value(self):
        return int.from_bytes(self.data_bytes[-4:], 'big')

    def read_max(self):
        return int.from_bytes(self.data_bytes[-8:-4], 'big')

    def read_min(self):
        return int.from_bytes(self.data_bytes[-4:], 'big')

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(UInt32Service, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help


class UInt64Service(SAServiceBase):
    ID = 0x0D

    def read_value(self):
        return int.from_bytes(self.data_bytes[-8:], 'big')

    def read_max(self):
        return int.from_bytes(self.data_bytes[-16:-8], 'big')

    def read_min(self):
        return int.from_bytes(self.data_bytes[-8:], 'big')

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(UInt64Service, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help


class Int8Service(SAServiceBase):
    ID = 0x0F

    def read_value(self):
        return int.from_bytes(self.data_bytes[-1:], 'big', signed=True)

    def read_max(self):
        return int.from_bytes(self.data_bytes[-2:-1], 'big', signed=True)

    def read_min(self):
        return int.from_bytes(self.data_bytes[-1:], 'big', signed=True)

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(Int8Service, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help


class Int16Service(SAServiceBase):
    ID = 0x10

    def read_value(self):
        return int.from_bytes(self.data_bytes[-2:], 'big', signed=True)

    def read_max(self):
        return int.from_bytes(self.data_bytes[-4:-2], 'big', signed=True)

    def read_min(self):
        return int.from_bytes(self.data_bytes[-2:], 'big', signed=True)

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(Int16Service, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help


class Int32Service(SAServiceBase):
    ID = 0x11

    def read_value(self):
        return int.from_bytes(self.data_bytes[-4:], 'big', signed=True)

    def read_max(self):
        return int.from_bytes(self.data_bytes[-4:-2], 'big', signed=True)

    def read_min(self):
        return int.from_bytes(self.data_bytes[-2:], 'big', signed=True)

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(Int32Service, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        return _help


class MDService(SAServiceBase):
    ID = 0x14

    def read_value(self):
        return (int.from_bytes(self.data_bytes[-2:1], 'big'),
                int.from_bytes(self.data_bytes[-1:], 'big'))

    def read_month(self):
        return self.read_value()[0]

    def read_day(self):
        return self.read_value()[1]

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(MDService, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        _help.update_kwargs_params({
            '<month>,<day>': '月日(M-D)'
        })
        return _help


class HMService(SAServiceBase):
    ID = 0x15

    def read_value(self):
        return (int.from_bytes(self.data_bytes[-2:1], 'big'),
                int.from_bytes(self.data_bytes[-1:], 'big'))

    def read_hour(self):
        return self.read_value()[0]

    def read_minute(self):
        return self.read_value()[1]

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(HMService, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        _help.update_kwargs_params({
            '<hour>,<minute>': '時分(H-M)'
        })
        return _help


class MSService(SAServiceBase):
    ID = 0x16

    def read_value(self):
        return (int.from_bytes(self.data_bytes[-2:1], 'big'),
                int.from_bytes(self.data_bytes[-1:], 'big'))

    def read_minute(self):
        return self.read_value()[0]

    def read_second(self):
        return self.read_value()[1]

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(MSService, self).to_cmd_help()
        _help.update_kwargs_type(self.__class__.__name__.replace('Service', ''))
        _help.update_kwargs_params({
            '<minute>,<second>': '分秒(M-S)'
        })
        return _help


class YMDHMSService(SAServiceBase):
    """todo"""
    ID = 0x17

    def read_value(self):
        raise NotImplementedError


class YMDHMService(SAServiceBase):
    """todo"""
    ID = 0x18

    def read_value(self):
        raise NotImplementedError


class StringService(SAServiceBase):
    """todo"""
    ID = 0x20

    def read_value(self):
        raise NotImplementedError


def query_sa_data_type_dynamic_len(data_type_id: int):
    if data_type_id in [SADataValueType.ENUM16,
                        SADataValueType.ENUM16_BIT,
                        SADataValueType.UNIT8,
                        SADataValueType.INT8,
                        SADataValueType.TIME_MD,
                        SADataValueType.TIME_HM,
                        SADataValueType.TIME_MS]:
        return 2
    elif data_type_id in [SADataValueType.UINT16,
                          SADataValueType.INT16]:
        return 4
    elif data_type_id in [SADataValueType.TIME_YMDHM]:
        return 5
    elif data_type_id in [SADataValueType.TIME_YMDHMS]:
        return 6
    elif data_type_id in [SADataValueType.UINT32,
                          SADataValueType.INT32]:
        return 8
    elif data_type_id in [SADataValueType.UINT64]:
        return 16
    elif data_type_id in [SADataValueType.STR]:
        return -1
    else:
        raise ValueError(f'data_type_id invalid, {data_type_id}')


__all__ = [
    'query_sa_data_type_dynamic_len',
    'SADataValueType',
    'SACmdHelp',
    'SAServiceBase',
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
    'MSService',
]
