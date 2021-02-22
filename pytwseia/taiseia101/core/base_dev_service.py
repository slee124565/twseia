
from base_obj import *

import struct
import logging
logger = logging.getLogger(__name__)


class DataTypeCode(BaseObject):
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


class DeviceBaseService(BasePdu):
    cmd_type_code = None  # read or write
    # service_data = None
    high_byte = None
    low_byte = None

    def __init__(self, pdu=None):
        if type(pdu) is list:
            super(DeviceBaseService, self).__init__(pdu)

            self.cmd_type_code = CmdTypeCode.get_code(pdu[2])
            self.service_id = pdu[2] & 0x7f
            self.high_byte = pdu[3]
            self.low_byte = pdu[4]

    def __str__(self):
        serv_param_code_cls = getattr(self.__class__, 'ParamCode', None)
        if self.high_byte == 0xff and self.low_byte == 0xff:
            value_text = 'ERROR'
        else:
            value_text = self.get_value()
            if serv_param_code_cls:
                value_text = serv_param_code_cls.text(self.get_value())
        return '{}({}, {})'.format(self.__class__.__name__,
                                   CmdTypeCode.text(self.cmd_type_code),
                                   value_text)

    @classmethod
    def read_txt_cmd(cls):
        raise Exception('{} classmethod read_txt_cmd not implemented'.format(cls.__name__))

    @classmethod
    def write_txt_cmd(cls, param=None):
        raise Exception('{} classmethod write_txt_cmd not implemented'.format(cls.__name__))

    def get_value(self):
        return self.high_byte * 0x100 + self.low_byte

    def to_spec(self):
        cmd_info = 'R'
        if self.cmd_type_code == CmdTypeCode.WRITE:
            cmd_info = 'RW'
        return '{}(code 0x{:02x}, {}, min {}, max {})'.format(
            self.__class__.__name__, self.service_id, cmd_info, self.high_byte, self.low_byte)

    def to_pdu(self):
        return [((self.cmd_type_code << 7) | self.service_id),
                self.high_byte, self.low_byte]

    def to_json(self):
        data = {
            'cmd_type_code': self.cmd_type_code,
            'service_id':  self.service_id,
            # 'high_byte': self.high_byte,
            # 'low_byte': self.low_byte
        }
        if self.high_byte is not None:
            data['high_byte'] = self.high_byte
        if self.low_byte is not None:
            data['low_byte'] = self.low_byte
        return data


class DeviceDataService(DeviceBaseService):
    """for device with data_kind_code is DeviceBaseService.DataKindCode.MULTIPLE"""
    data_type_id = None
    # data_len = None
    # datas = None
    data_pdu = None

    def __init__(self, pdu=None):
        super(DeviceDataService, self).__init__(pdu)
        # self.high_byte = self.low_byte = None
        self.data_type_id = pdu[1]
        self.data_pdu = pdu[2:]

    def to_json(self):
        data = super(DeviceDataService, self).to_json()
        if self.data_type_id is not None:
            data['data_type_id'] = self.data_type_id
        if self.data_pdu is not None:
            data['data_hex'] = get_byte_list_hex_str(self.data_pdu)
        return data


class DeviceEnum16Service(DeviceBaseService):
    pass


class DeviceCommonOnOffService(DeviceEnum16Service):
    class ParamCode(BaseObject):
        OFF = 0
        ON = 1


class DeviceFeatureLevelService(DeviceEnum16Service):

    class ParamCode(BaseObject):
        LEVEL_0 = 0
        LEVEL_1 = 1
        LEVEL_2 = 2
        LEVEL_3 = 3
        LEVEL_4 = 4
        LEVEL_5 = 5
        LEVEL_6 = 6
        LEVEL_7 = 7
        LEVEL_8 = 8
        LEVEL_9 = 9
        LEVEL_10 = 10
        LEVEL_11 = 11
        LEVEL_12 = 12
        LEVEL_13 = 13
        LEVEL_14 = 14
        LEVEL_15 = 15

        @classmethod
        def text(cls, code):
            return 'level {}'.format(code)


class DeviceEnum16BitService(DeviceBaseService):

    def get_value(self):
        value = super(DeviceEnum16BitService, self).get_value()
        return '{:016}'.format(value)

    def get_enum_bit_value(self, bit_index):
        if 0 <= bit_index <= 7:
            mask = 1 << bit_index
            return (self.low_byte & mask) >> bit_index
        elif 8 <= bit_index <= 15:
            mask = 1 << (bit_index-8)
            return (self.low_byte & mask) >> (bit_index-8)
        else:
            raise ValueError('{} bit_index {} error'.format(self.__class__.__name__, bit_index))


class DeviceUint8Service(DeviceBaseService):

    def get_value(self):
        return struct.unpack('B', chr(self.low_byte))[0]


class DeviceUint16Service(DeviceBaseService):
    pass


class DeviceInt8Service(DeviceBaseService):

    def get_value(self):
        return struct.unpack('b', chr(self.low_byte))[0]


class DeviceTimeMDService(DeviceBaseService):

    def get_value(self):
        return self.high_byte, self.low_byte

    def get_month_value(self):
        return self.high_byte

    def get_day_value(self):
        return self.low_byte


class DeviceTimeHMService(DeviceBaseService):

    def get_value(self):
        return self.high_byte, self.low_byte

    def get_hour_value(self):
        return self.high_byte

    def get_minute_value(self):
        return self.low_byte


class DeviceTimeMSService(DeviceBaseService):

    def get_value(self):
        return self.high_byte, self.low_byte

    def get_minute_value(self):
        return self.high_byte

    def get_second_value(self):
        return self.low_byte
