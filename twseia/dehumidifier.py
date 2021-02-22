from twseia.taiseia101.core import *

logger = logging.getLogger(__name__)


class Dehumidifier(GeneralDevice):
    dev_type = {'id': DeviceTypeCode.DEHUMIDIFIER, 'name': 'DEHUMIDIFIER'}

    class ServiceCode(BaseObject):
        POWER_RW = 0x00
        OP_MODE_RW = 0x01
        OP_TIMER_RW = 0x02
        HUMIDITY_CFG_RW = 0x03
        DEHUMIDIFIER_LEVEL_RW = 0x04
        DRY_CLOTHE_LEVEL_RW = 0x05
        TEMPERATURE_R = 0x06
        HUMIDITY_R = 0x07
        FAN_DIRECTION_AUTO_RW = 0x08
        FAN_DIRECTION_LEVEL_RW = 0x09
        WATER_FULL_ALARM_R = 0x0a
        FILTER_CLEAN_NOTIFY_RW = 0x0b
        MOOD_LED_RW = 0x0c
        AIR_CLEAN_MODE_RW = 0x0d
        FAN_LEVEL_RW = 0x0e
        SIDE_FAN_R = 0x0f
        AUDIO_RW = 0x10
        DEFROST_DISPLAY_R = 0x11
        DISPLAY_ERR_R = 0x12
        DEV_MILDEW_RW = 0x13
        HUMIDITY_HIGH_NOTIFY_RW = 0x14
        HUMIDITY_HIGH_CFG_RW = 0x15
        KEYPAD_LOCK_RW = 0x16
        REMOTE_CTRL_LOCK_RW = 0x17
        SAA_CTRL_AUDIO_RW = 0x18
        OP_CURRENT_R = 0x19
        OP_VOLTAGE_R = 0x1a
        OP_POWER_FACTOR_R = 0x1b
        OP_POWER_WATT_RW = 0x1c
        TOTAL_WATT_RW = 0x1d
        ERR_HISTORY_1_R = 0x1e
        ERR_HISTORY_2_R = 0x1f
        ERR_HISTORY_3_R = 0x20
        ERR_HISTORY_4_R = 0x21
        ERR_HISTORY_5_R = 0x22
        # ENG_MODE = 0x50
        # RESERVED = 0x7f

    def __init__(self):
        super(Dehumidifier, self).__init__()
        self.set_dev_type(DeviceTypeCode.DEHUMIDIFIER)

    @classmethod
    def module_name(cls):
        return __name__


class DevicePowerService(DeviceCommonOnOffService):
    """
    status off: 06,04,00,00,00,02
    status on: 06,04,00,00,01,03
    power on: 06,04,80,00,01,83
    power off: 06,04,80,00,00,82
    """
    # POWER_RW = 0x00


class DeviceOpModeService(DeviceEnum16Service):
    # OP_MODE_RW = 0x01

    class ParamCode(BaseObject):
        AUTO = 0
        CFG_DEHUMIDIFIER = 1
        CONTINUE_DEHUMIDIFIER = 2
        DRY_CLOTHE = 3
        AIR_CLEAN = 4
        DEV_MILDEW = 5
        FAN_ONLY = 6
        SUPER_DRY = 7


class DeviceOpTimerService(DeviceUint8Service):
    # OP_TIMER_RW = 0x02

    class ParamCode(BaseObject):
        HR_1 = 1
        HR_2 = 2
        HR_4 = 4
        HR_6 = 6
        HR_8 = 8
        HR_10 = 10
        HR_12 = 12

        @classmethod
        def text(cls, code):
            return '{} hr'.format(code)


class DeviceHumidityCfgService(DeviceUint8Service):
    # HUMIDITY_CFG_RW = 0x03

    class ParamCode(BaseObject):
        HUMI_40 = 40
        HUMI_45 = 45
        HUMI_50 = 50
        HUMI_55 = 55
        HUMI_60 = 60
        HUMI_65 = 65
        HUMI_70 = 70
        HUMI_75 = 75

        @classmethod
        def text(cls, code):
            return '{} %'.format(code)


class DeviceDehumidifierLevelService(DeviceFeatureLevelService):
    # DEHUMIDIFIER_LEVEL_RW = 0x04
    pass


class DeviceDryClotheLevelService(DeviceFeatureLevelService):
    # DRY_CLOTHE_LEVEL_RW = 0x05
    pass


class DeviceTemperatureRService(DeviceInt8Service):
    # TEMPERATURE_R = 0x06
    pass


class DeviceHumidityRService(DeviceUint8Service):
    # HUMIDITY_R = 0x07
    pass


class DeviceFanDirectionAutoService(DeviceCommonOnOffService):
    # FAN_DIRECTION_AUTO_RW = 0x08
    pass


class DeviceFanDirectionLevelService(DeviceFeatureLevelService):
    # FAN_DIRECTION_LEVEL_RW = 0x09
    pass


class DeviceWaterFullAlarmRService(DeviceEnum16Service):
    # WATER_FULL_ALARM_R = 0x0a
    class ParamCode(BaseObject):
        NORMAL = 0x00
        FULL = 0x01

    pass


class DeviceFilterCleanNotifyService(DeviceEnum16Service):
    # FILTER_CLEAN_NOTIFY_RW = 0x0b
    class ParamCode(BaseObject):
        NORMAL = 0x00
        CLEAN_NEED = 0x01

    pass


class DeviceMoodLedService(DeviceCommonOnOffService):
    # MOOD_LED_RW = 0x0c
    pass


class DeviceAirCleanModeService(DeviceFeatureLevelService):
    # AIR_CLEAN_MODE_RW = 0x0d
    pass


class DeviceFanLevelService(DeviceFeatureLevelService):
    pass  # FAN_LEVEL_RW = 0x0e


class DeviceSideFanRService(DeviceEnum16Service):
    # SIDE_FAN_R = 0x0f
    class ParamCode(BaseObject):
        NORMAL = 0x00
        SIDE = 0x01

    pass


class DeviceAudioService(DeviceEnum16Service):
    # AUDIO_RW = 0x10
    class ParamCode(BaseObject):
        QUIET = 0x00
        BUTTON = 0x01
        WATER_FULL_BUTTON = 0x02

    pass


class DeviceDefrostDisplayRService(DeviceEnum16Service):
    # DEFROST_DISPLAY_R = 0x11
    class ParamCode(BaseObject):
        NORMAL = 0x00
        DEFROST = 0x01

    pass


class DeviceDisplayErrRService(DeviceEnum16BitService):
    # DISPLAY_ERR_R = 0x12
    pass


class DeviceDevMildewService(DeviceCommonOnOffService):
    # DEV_MILDEW_RW = 0x13
    pass


class DeviceHumidityHighNotifyService(DeviceCommonOnOffService):
    # HUMIDITY_HIGH_NOTIFY_RW = 0x14
    pass


class DeviceHumidityHighCfgService(DeviceUint8Service):
    # HUMIDITY_HIGH_CFG_RW = 0x15
    pass


class DeviceKeypadLockService(DeviceCommonOnOffService):
    # KEYPAD_LOCK_RW = 0x16
    pass


class DeviceRemoteCtrlLockService(DeviceEnum16BitService):
    # REMOTE_CTRL_LOCK_RW = 0x17
    pass


class DeviceSaaCtrlAudioService(DeviceCommonOnOffService):
    # SAA_CTRL_AUDIO_RW = 0x18
    pass


class DeviceOpCurrentRService(DeviceUint16Service):
    # OP_CURRENT_R = 0x19
    pass


class DeviceOpVoltageRService(DeviceUint16Service):
    # OP_VOLTAGE_R = 0x1a
    pass


class DeviceOpPowerFactorRService(DeviceUint16Service):
    # OP_POWER_FACTOR_R = 0x1b
    pass


class DeviceOpPowerWattService(DeviceUint16Service):
    # OP_POWER_WATT_RW = 0x1c
    pass


class DeviceTotalWattService(DeviceUint16Service):
    # TOTAL_WATT_RW = 0x1d
    pass


class DeviceErrHistory1RService(DeviceEnum16BitService):
    # ERR_HISTORY_1_R = 0x1e
    pass


class DeviceErrHistory2RService(DeviceEnum16BitService):
    # ERR_HISTORY_2_R = 0x1f
    pass


class DeviceErrHistory3RService(DeviceEnum16BitService):
    # ERR_HISTORY_3_R = 0x20
    pass


class DeviceErrHistory4RService(DeviceEnum16BitService):
    # ERR_HISTORY_4_R = 0x21
    pass


class DeviceErrHistory5RService(DeviceEnum16BitService):
    # ERR_HISTORY_5_R = 0x22
    pass


if __name__ == '__main__':
    FORMAT = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    dev_cls = Dehumidifier
    # dev_cls.print_service_cls_template()
    dev_obj = dev_cls()
    logger.info('{}'.format(dev_obj.device_detail(cmd_check_serv=False)))
