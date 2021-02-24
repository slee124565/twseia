
from .base_obj import *
from .base_dev_service import *

import logging
logger = logging.getLogger(__name__)


# class DeviceTypeCode(BaseObject):
#     REGISTER = 0x00
#     AIR_CONDITIONER = 0x01
#     REFRIGERATOR = 0x02
#     WATCHING_MACHINE = 0x03
#     DEHUMIDIFIER = 0x04
#     TELEVISION = 0X05
#     DRYING_MACHINE = 0X06
#     HEAD_PUMP_WATER_HEATER = 0X07
#     AIR_CLEANER = 0X08
#     ELECTRONIC_POT = 0X09
#     OPEN_DRINK_MACHINE = 0X0A
#     INDUCTION_COOKER = 0X0B
#     DISH_WASHER = 0X0C
#     MICROWAVE_OVEN = 0X0D
#     FULL_HEAT_SWITCH = 0X0E
#     FAN = 0X0F
#     GAS_WATER_HEATER = 0X10
#     LAMP = 0X11
#     SMART_METER_GATEWAY = 0XE0
#     GENERAL_DEVICE = 0XF0
#     ERROR = 0XFF
#
#
# class BasePdu(BaseObject):
#     pdu = []  # pocket bytes list
#     length = 0  # pud length
#     dev_type_id = None  # DeviceTypeCode
#     service_id = None
#     datas = None  # byte list
#     check_sum = 0
#
#     def __init__(self, pdu=None):
#         if type(pdu) is list:
#             self.pdu = pdu
#             self.length = pdu[0]
#             if self.length != len(self.pdu):
#                 logger.warning('{} init pdu length field error'.format(self.__class__.__name__))
#
#             self.dev_type_id = pdu[1]
#             self.check_sum = pdu[-1]
#
#     def get_pdu_check_sum(self):
#         if type(self.pdu) is list and len(self.pdu) > 0:
#             self.pdu[0] = len(self.pdu)
#             for x in self.pdu[:-1]:
#                 self.pdu[-1] ^= x
#             return self.pdu[-1]
#         else:
#             raise ValueError('{} pdu type should be list')
#
#     def __str__(self):
#         if self.service_id:
#             return '{}(type {})'.format(
#                 self.__class__.__name__, DeviceTypeCode.text(self.dev_type_id))
#         else:
#             return '{}(type {})'.format(
#                 self.__class__.__name__, DeviceTypeCode.text(self.dev_type_id))
#
#     def to_json(self):
#         data = {
#             'dev_type_id': self.dev_type_id,
#         }
#         return data
#

class BaseRequest(BasePdu):
    cmd_code = None  # CmdType

    def __init__(self, dev_type_id, service_id, cmd_code=CmdTypeCode.READ, high_byte=0xff, low_byte=0xff):
        super(BaseRequest, self).__init__()
        self.length = 0x06  # fix array size pdu
        self.dev_type_id = dev_type_id
        self.service_id = service_id
        self.cmd_code = cmd_code
        self.datas = [high_byte & 0xff, low_byte & 0xff]

    def to_pdu(self):
        self.pdu = [0,
                    self.dev_type_id,
                    (self.cmd_code << 7) | self.service_id,
                    self.datas[0], self.datas[1],
                    self.check_sum
               ]
        self.pdu[0] = len(self.pdu)
        self.pdu[-1] = self.get_pdu_check_sum()
        # logger.debug('{} to_pdu {}'.format(self.__class__.__name__, self.pdu))
        return self.pdu

    def to_json(self):
        data = super(BaseRequest, self).to_json()
        data['cmd_code'] = self.cmd_code
        data['service_id'] = self.service_id,
        data['data_hex'] = get_byte_list_hex_str(self.datas),
        return data

    def to_hex(self):
        return get_byte_list_hex_str(self.to_pdu())

    def __str__(self):
        return '{}(type {}, cmd {}, serv {}, data_hex {})'.format(
            self.__class__.__name__,
            DeviceTypeCode.text(self.dev_type_id),
            CmdTypeCode.text(self.cmd_code), self.service_id,
            get_byte_list_hex_str(self.to_pdu())
        )


class BaseResponse(BasePdu):

    def __init__(self, pdu):
        super(BaseResponse, self).__init__(pdu)
        if self.dev_type_id != DeviceTypeCode.REGISTER:
            self.service_id = pdu[2] & 0x7f
            self.datas = pdu[3:-1]
        else:
            self.datas = pdu[2:-1]

    def to_json(self):
        data = super(BaseResponse, self).to_json()
        if self.service_id:
            data['service_id'] = self.service_id,
        data['data_hex'] = get_byte_list_hex_str(self.datas),
        return data

    def __str__(self):
        return '{}(type {}, serv {}, data_hex {})'.format(
            self.__class__.__name__,
            DeviceTypeCode.text(self.dev_type_id),
            self.service_id,
            get_byte_list_hex_str(self.datas)
        )


class ErrorResponse(BaseResponse):

    def __init__(self, pdu):
        super(ErrorResponse, self).__init__(pdu)


# class DeviceBaseService(BaseObject):
#     pdu = None
#     cmd_type_code = None  # read or write
#     service_id = None
#     service_data = None
#     # high_byte = None
#     # low_byte = None
#
#     def __init__(self, pdu=None):
#         self.pdu = pdu
#         self.cmd_type_code = CmdTypeCode.get_code(pdu[0])
#         self.service_id = pdu[0] & 0x7f
#         # self.high_byte = pdu[1]
#         # self.low_byte = pdu[2]
#
#     def __str__(self):
#         return '{}({})'.format(self.__class__.__name__, self.to_json())
#
#     def to_json(self):
#         data = {
#             'cmd_type_code': self.cmd_type_code,
#             'service_id':  self.service_id,
#             # 'high_byte': self.high_byte,
#             # 'low_byte': self.low_byte
#         }
#         # if self.high_byte:
#         #     data['high_byte'] = self.high_byte
#         # if self.low_byte:
#         #     data['low_byte'] = self.low_byte
#         return data
#
#
# class DeviceDataService(DeviceBaseService):
#     """for device with data_kind_code is DeviceBaseService.DataKindCode.MULTIPLE"""
#     data_type_id = None
#     # data_len = None
#     # datas = None
#
#     def __init__(self, pdu=None):
#         super(DeviceDataService, self).__init__(pdu)
#         # self.high_byte = self.low_byte = None
#         self.data_type_id = pdu[1]
#         # self.datas = pdu[2:]
#
#     def to_json(self):
#         data = super(DeviceDataService, self).to_json()
#         if self.data_type_id:
#             data['data_type_id'] = self.data_type_id
#         # if self.datas:
#         #     data['data_hex'] = get_byte_list_hex_str(self.datas)
#         return data
#
# base_dev_service
class DeviceRegisterService(DeviceBaseService):

    class ServiceCode(BaseObject):
        """deprecated by SAServiceID"""
        REGISTER = 0X00
        READ_DEVICE_CLASS_ID = 0X01
        READ_DEVICE_PROTOCOL_VER = 0X02
        RESERVED = 0X03
        READ_DEVICE_TYPE_ID = 0X04
        READ_DEVICE_BRAND = 0X05
        READ_DEVICE_MODEL = 0X06
        READ_DEVICE_SERVICES = 0X07
        READ_DEVICE_SERVICES_STATUS = 0X08

    def __init__(self):
        super(DeviceRegisterService, self).__init__()
        self.cmd_type_code = CmdTypeCode.READ
        self.service_id = DeviceRegisterService.ServiceCode.REGISTER
        self.high_byte = 0xff
        self.low_byte = 0xff


class RegisterResponse(BaseResponse):
    # dev_type_id = None  # DeviceTypeCode
    # service_id = None
    # datas = None  # byte list
    data_kind_code = None  # DataKinkCode
    dev_class_code = None
    major_ver = None  # protocol major version
    minor_ver = None  # protocol minor version
    offset = None  # fragment offset
    dev_brand = None
    dev_model = None
    services = {}

    class DataKindCode(BaseObject):
        GENERAL = 0x00
        MULTIPLE = 0x01

        @classmethod
        def get_code(cls, byte_value):
            return (byte_value & 0x80) >> 7

    class DeviceClassCode(BaseObject):
        """deprecated by SAClassID"""
        HOME_DEVICE = 0x00
        POWER_DEVICE = 0x01
        ENERGY_STORAGE_DEVICE = 0x02
        SENSOR_DEVICE = 0x03

        @staticmethod
        def get_code(byte_value):
            return byte_value & 0x0f

    def __init__(self, pdu):
        super(RegisterResponse, self).__init__(pdu)

        self.data_kind_code = RegisterResponse.DataKindCode.get_code(pdu[2])
        self.dev_class_code = RegisterResponse.DeviceClassCode.get_code(pdu[2])
        self.major_ver = pdu[3]
        self.minor_ver = pdu[4]
        self.offset = pdu[5]
        self.dev_type_id = pdu[6] * 0x100 + pdu[7]

        n_zero = pdu[8:].index(0)
        self.dev_brand = bytearray(pdu[8:8+n_zero]).decode("utf-8")

        n_start = 8 + n_zero + 1
        n_zero = pdu[n_start:].index(0)
        self.dev_model = bytearray(pdu[n_start:n_start+n_zero]).decode("utf-8")

        n_start = n_start+n_zero+1
        self.datas = pdu[n_start:-1]

    def to_json(self):
        data = super(RegisterResponse, self).to_json()
        if 'data_hex' in data.keys():
            del data['data_hex']
        data['data_kind_code'] = self.data_kind_code
        data['dev_class_code'] = self.dev_class_code
        data['major_ver'] = self.major_ver
        data['minor_ver'] = self.minor_ver
        data['offset'] = self.offset
        data['dev_brand'] = self.dev_brand
        data['dev_model'] = self.dev_model
        data['services'] = {}
        for key, service in self.services.items():
            data['services'][key] = service.to_json()
        return data

    def __str__(self):
        return '{}({}, {} {}, {}.{})'.format(
            self.__class__.__name__,
            RegisterResponse.DeviceClassCode.text(self.dev_class_code),
            self.dev_brand, self.dev_brand, self.major_ver, self.minor_ver)


class RegisterRequest(BaseRequest):

    def __init__(self):
        super(RegisterRequest, self).__init__(
            DeviceTypeCode.REGISTER, DeviceRegisterService.ServiceCode.REGISTER)


class BaseReadRequest(BaseRequest):

    def __init__(self, service_id, dev_type_id=0x00, high_byte=0xff, low_byte=0xff):
        super(BaseReadRequest, self).__init__(
            dev_type_id=dev_type_id, service_id=service_id,
            high_byte=high_byte, low_byte=low_byte)


class BaseReadResponse(BaseResponse):
    pass


class DataReadRequest(BaseReadRequest):
    """for device with data_kind_code is DeviceBaseService.DataKindCode.MULTIPLE"""
    data_type_id = None

    def __init__(self, dev_type_id, service_id, data_type_id, datas):
        super(DataReadRequest, self).__init__(dev_type_id=dev_type_id, service_id=service_id)
        self.data_type_id = data_type_id
        self.datas = datas


class DataReadResponse(BaseReadResponse):
    """for device with data_kind_code is DeviceBaseService.DataKindCode.MULTIPLE"""
    data_type_id = None

    def __init__(self, pdu):
        super(DataReadResponse, self).__init__(pdu)
        self.data_type_id = self.datas[0]
        self.datas = self.datas[1:]


class SensorReadRequest(DataReadRequest):
    pass


class SensorReadResponse(DataReadResponse):
    offset = None

    def __init__(self, pdu):
        super(SensorReadResponse, self).__init__(pdu)
        self.offset = self.datas[0] * 0x100 + self.datas[1]
        self.datas = self.datas[2:]


class BaseWriteRequest(BaseReadRequest):

    def __init__(self, dev_type_id, service_id, high_byte, low_byte):
        super(BaseWriteRequest, self).__init__(
            dev_type_id=dev_type_id, service_id=service_id,
            high_byte=high_byte, low_byte=low_byte)
        self.cmd_code = CmdTypeCode.WRITE


class BaseWriteResponse(BaseReadResponse):

    def __init__(self, pdu):
        super(BaseWriteResponse, self).__init__(pdu)
        self.service_id = self.service_id & 0x7f
