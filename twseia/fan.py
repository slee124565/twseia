from twseia.taiseia101.core import *

logger = logging.getLogger(__name__)


class Fan(GeneralDevice):
    dev_type = {'id': DeviceTypeCode.FAN, 'name': 'FAN'}

    class ServiceCode(BaseObject):
        POWER_RW = 0x00
        OP_MODE_RW = 0x01
        FAN_LEVEL_RW = 0x02
        TEMPERATURE_R = 0x03
        COMFORTABLE_TIMER_RW = 0x04
        FAN_SWING_RW = 0x05
        ANION_CFG_RW = 0x06
        LIGHT_CFG_RW = 0x07
        HUMIDITY_R = 0x08
        CLOCK_ON_RW = 0x09
        CLOCK_OFF_RW = 0x0a
        TIMER_ON_RW = 0x0b
        TIMER_OFF_RW = 0x0c
        SYS_TIME_RW = 0x0d
        OP_CURRENT_R = 0x0e
        OP_VOLTAGE_R = 0x0f
        OP_POWER_FACTOR_R = 0x10
        INSTANT_WATT_R = 0x11
        TOTAL_WATT_RW = 0x12
        ERR_HISTORY_1_R = 0x13
        ERR_HISTORY_2_R = 0x14
        ERR_HISTORY_3_R = 0x15
        ERR_HISTORY_4_R = 0x16
        ERR_HISTORY_5_R = 0x17

    def __init__(self):
        super(Fan, self).__init__()
        self.set_dev_type(DeviceTypeCode.FAN)

    @classmethod
    def module_name(cls):
        return __name__


class DevicePowerService(DeviceCommonOnOffService):
    # POWER_RW = 0x00
    pass


class DeviceOpModeService(DeviceEnum16Service):
    # OP_MODE_RW = 0x01
    class ParamCode(BaseObject):
        MODE_1 = 0x00
        MODE_2 = 0x01
        MODE_3 = 0x02
        MODE_4 = 0x03
        MODE_5 = 0x04

    pass


class DeviceFanLevelService(DeviceFeatureLevelService):
    # FAN_LEVEL_RW = 0x02
    pass


class DeviceTemperatureRService(DeviceInt8Service):
    # TEMPERATURE_R = 0x03
    pass


class DeviceComfortableTimerService(DeviceUint16Service):
    # COMFORTABLE_TIMER_RW = 0x04
    pass


class DeviceFanSwingService(DeviceCommonOnOffService):
    # FAN_SWING_RW = 0x05
    pass


class DeviceAnionCfgService(DeviceCommonOnOffService):
    # ANION_CFG_RW = 0x06
    pass


class DeviceLightCfgService(DeviceCommonOnOffService):
    # LIGHT_CFG_RW = 0x07
    pass


class DeviceHumidityRService(DeviceUint8Service):
    # HUMIDITY_R = 0x08
    pass


class DeviceClockOnService(DeviceTimeHMService):
    # CLOCK_ON_RW = 0x09
    pass


class DeviceClockOffService(DeviceTimeHMService):
    # CLOCK_OFF_RW = 0x0a
    pass


class DeviceTimerOnService(DeviceUint16Service):
    # TIMER_ON_RW = 0x0b
    pass


class DeviceTimerOffService(DeviceUint16Service):
    # TIMER_OFF_RW = 0x0c
    pass


class DeviceSysTimeService(DeviceTimeHMService):
    # SYS_TIME_RW = 0x0d
    pass


class DeviceOpCurrentRService(DeviceUint16Service):
    # OP_CURRENT_R = 0x0e
    pass


class DeviceOpVoltageRService(DeviceUint16Service):
    # OP_VOLTAGE_R = 0x0f
    pass


class DeviceOpPowerFactorRService(DeviceUint16Service):
    # OP_POWER_FACTOR_R = 0x10
    pass


class DeviceInstantWattRService(DeviceUint16Service):
    # INSTANT_WATT_R = 0x11
    pass


class DeviceTotalWattService(DeviceUint16Service):
    # TOTAL_WATT_RW = 0x12
    pass


class DeviceErrHistory1RService(DeviceEnum16BitService):
    # ERR_HISTORY_1_R = 0x13
    pass


class DeviceErrHistory2RService(DeviceEnum16BitService):
    # ERR_HISTORY_2_R = 0x14
    pass


class DeviceErrHistory3RService(DeviceEnum16BitService):
    # ERR_HISTORY_3_R = 0x15
    pass


class DeviceErrHistory4RService(DeviceEnum16BitService):
    # ERR_HISTORY_4_R = 0x16
    pass


class DeviceErrHistory5RService(DeviceEnum16BitService):
    # ERR_HISTORY_5_R = 0x17
    pass


if __name__ == '__main__':
    FORMAT = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    dev_cls = Fan
    # dev_cls.print_service_cls_template()
    dev_obj = dev_cls()
    logger.info('{}'.format(dev_obj.device_detail(cmd_check_serv=False)))
