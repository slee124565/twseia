# -*- coding: utf-8 -*-
import enum


class SATypeIDEnum(enum.IntEnum):
    """SA類別碼, TAISEIA Spec. Table_10"""
    REGISTER = 0x00
    """註冊用"""
    AIR_CONDITIONER = 0x01
    """冷氣機"""
    REFRIGERATOR = 0x02
    """電冰箱"""
    WATCHING_MACHINE = 0x03
    """洗衣機"""
    DEHUMIDIFIER = 0x04
    """除濕機"""
    TELEVISION = 0x05
    """電視機"""
    DRYING_MACHINE = 0x06
    """烘衣機"""
    HEAD_PUMP_WATER_HEATER = 0x07
    """熱泵熱水器"""
    AIR_CLEANER = 0x08
    """空氣清淨機"""
    ELECTRONIC_POT = 0x09
    """電子鍋"""
    OPEN_DRINK_MACHINE = 0x0A
    """開飲機"""
    INDUCTION_COOKER = 0x0B
    """電磁爐"""
    DISH_WASHER = 0x0C
    """烘碗機"""
    MICROWAVE_OVEN = 0x0D
    """微波爐"""
    FULL_HEAT_SWITCH = 0x0E
    """全熱交換器"""
    FAN = 0x0F
    """電扇"""
    GAS_WATER_HEATER = 0x10
    """燃氣熱水器"""
    LAMP = 0x11
    """燈具"""
    # FAN_SAMPO = 0x13
    SMART_METER_GATEWAY = 0xE0
    """智慧電表閘道器"""
    GENERAL_DEVICE = 0xF0
    """通用裝置"""


class SARegisterServiceIDEnum(enum.IntEnum):
    """ SA註冊用服務類別, TAISEIA Spec. Table_14"""
    REGISTRATION = 0X00
    """註冊服務"""
    READ_CLASS_ID = 0X01
    """讀取裝置類別代碼(Class ID) """
    READ_PROTOCOL_VERSION = 0X02
    """讀取TaiSEIA 101裝置監控通訊協定版本值 """
    RESERVED = 0X03
    """保留, 保留供未來擴充功能使用"""
    READ_TYPE_ID = 0X04
    """讀取SA類別代碼(Type ID) """
    READ_BRAND = 0X05
    """讀取SA廠牌(Brand) """
    READ_MODEL = 0X06
    """讀取SA型號(Model) """
    READ_SUPPORTED_SERVICES = 0X07
    """讀取SA可提供之所有支援服務規格 """
    READ_CURRENT_SERVICES_STATES = 0X08
    """讀取SA目前所有服務狀態值"""


class SAServiceIOMode(enum.IntEnum):
    """SA服務類別讀/寫(R/W)功能規格"""
    READ = 0x00
    READ_WRITE = 0x01


class SAClassID(enum.IntEnum):
    """SA裝置類別: 0：家庭電器、1：發電設備、2：儲能設備、3：感測設備。"""
    HOME_DEVICE = 0x00
    POWER_GENERATION_DEVICE = 0x01
    ENERGY_STORAGE_DEVICE = 0x02
    SENSOR_DEVICE = 0x03


class SAPacketDataLenType(enum.IntEnum):
    """多位元組資料型態SA：0代表一般資料型態SA、1代表多位元組資料型態SA"""
    FIXED_LEN = 0
    DYNAMIC_LEN = 1
