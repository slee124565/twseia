

import inspect
import logging
logger = logging.getLogger(__name__)


def get_byte_list_hex_str(datas):
    if type(datas) is list:
        return '{}'.format(', '.join('0x{:02x}'.format(x) for x in datas))
    else:
        return str(datas)


class BaseObject(object):
    @classmethod
    def text(cls, code):
        members = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
        for member in members:
            if member[1] == code:
                return member[0]
        return code

    @classmethod
    def inspect_code_members(cls):
        members = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
        codes = []
        for member in members:
            if str(member[0]).find('__') != 0:
                codes.append(member)
        codes.sort(key=lambda x: x[1])
        return codes


class CmdTypeCode(BaseObject):
    READ = 0
    WRITE = 1

    @staticmethod
    def get_code(byte_value):
        return byte_value >> 7


class DeviceTypeCode(BaseObject):
    """deprecated by SATypeID class"""
    REGISTER = 0x00
    AIR_CONDITIONER = 0x01
    REFRIGERATOR = 0x02
    WATCHING_MACHINE = 0x03
    DEHUMIDIFIER = 0x04
    TELEVISION = 0x05
    DRYING_MACHINE = 0x06
    HEAD_PUMP_WATER_HEATER = 0x07
    AIR_CLEANER = 0x08
    ELECTRONIC_POT = 0x09
    OPEN_DRINK_MACHINE = 0x0A
    INDUCTION_COOKER = 0x0B
    DISH_WASHER = 0x0C
    MICROWAVE_OVEN = 0x0D
    FULL_HEAT_SWITCH = 0x0E
    FAN = 0x0F
    GAS_WATER_HEATER = 0x10
    LAMP = 0x11
    SAMPOFAN = 0x13
    SMART_METER_GATEWAY = 0xE0
    GENERAL_DEVICE = 0xF0
    ERROR = 0xFF


class BasePdu(BaseObject):
    pdu = []  # pocket bytes list
    length = 0  # pud length
    dev_type_id = None  # DeviceTypeCode
    service_id = None
    datas = None  # byte list
    check_sum = 0

    def __init__(self, pdu=None):
        if type(pdu) is list:
            self.pdu = pdu
            self.length = pdu[0]
            if self.length != len(self.pdu):
                logger.warning('{} init pdu length field error'.format(self.__class__.__name__))

            self.dev_type_id = pdu[1]
            self.check_sum = pdu[-1]

    def get_pdu_check_sum(self):
        if type(self.pdu) is list and len(self.pdu) > 0:
            self.pdu[0] = len(self.pdu)
            for x in self.pdu[:-1]:
                self.pdu[-1] ^= x
            return self.pdu[-1]
        else:
            raise ValueError('{} pdu type should be list')

    def __str__(self):
        if self.service_id:
            return '{}(type {})'.format(
                self.__class__.__name__, DeviceTypeCode.text(self.dev_type_id))
        else:
            return '{}(type {})'.format(
                self.__class__.__name__, DeviceTypeCode.text(self.dev_type_id))

    def to_json(self):
        data = {
            'dev_type_id': self.dev_type_id,
        }
        return data
