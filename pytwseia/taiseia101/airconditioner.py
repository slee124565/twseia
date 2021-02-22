from .core import *

logger = logging.getLogger(__name__)


class AirConditioner(GeneralDevice):
    dev_type = {'id': DeviceTypeCode.AIR_CONDITIONER, 'name': 'AIR_CONDITIONER'}

    class ServiceCode(BaseObject):
        POWER_RW = 0x00
        OP_MODE_RW = 0x01
        FAN_LEVEL_RW = 0x02
        TEMPERATURE_CFG_RW = 0x03
        TEMPERATURE_R = 0x04
        COMFORTABLE_RW = 0x05
        COMFORTABLE_TIMER_RW = 0x06
        FUZZY_TEMPERATURE_RW = 0x07
        AIR_CLEAN_MODE_RW = 0x08
        CLOCK_ON_RW = 0x09
        CLOCK_OFF_RW = 0x0a
        TIMER_ON_RW = 0x0b
        TIMER_OFF_RW = 0x0c
        SYS_TIME_RW = 0x0d
        FAN_UPDOWN_RW = 0x0e
        FAN_UPDOWN_LEVEL_RW = 0x0f
        FAN_SWING_RW = 0x10
        FAN_SWING_LEVEL_RW = 0x11
        FILTER_CLEAN_NOTIFY_RW = 0x12
        DEHUMIDIFIER_CFG_RW = 0x13
        HUMIDITY_R = 0x14
        SYS_CHECK_R = 0x15
        AIR_DETECT_RW = 0x16
        DEV_MILDEW_RW = 0x17
        SELF_CLEAN_RW = 0x18
        MOTION_DETECT_MODE_RW = 0x19
        FAST_OP_RW = 0x1a
        POWER_SAVING_OP_RW = 0x1b
        POWER_LIMIT_OP_RW = 0x1c
        REMOTE_CTRL_LOCK_RW = 0x1d
        SAA_CTRL_AUDIO_RW = 0x1e
        BODY_DISPLAY_MODE_RW = 0x1f
        MOISTURIZE_MODE_RW = 0x20
        OUTDOOR_TEMPERATURE_R = 0x21
        INDOOR_UNIT_WATT_R = 0x22
        OUTDOOR_UNIT_WATT_R = 0x23
        OUTDOOR_UNIT_CURRENT_R = 0x24
        OUTDOOR_UNIT_VOLTATE_R = 0x25
        OUTDOOR_UNIT_POWER_FACTOR_R = 0x26
        OUTDOOR_UNIT_INSTANT_WATT_R = 0x27
        TOTAL_WATT_RW = 0x28
        DISPLAY_ERR_R = 0x29
        ERR_HISTORY_1_R = 0x2a
        ERR_HISTORY_2_R = 0x2b
        ERR_HISTORY_3_R = 0x2c
        ERR_HISTORY_4_R = 0x2d
        ERR_HISTORY_5_R = 0x2e
        MAINTENANCE_ACCU_OP_HOUR_RW = 0x2f
        FILTER_ACCU_OP_HOUR_RW = 0x30
        SYS_YEAR_RW = 0x31
        SYS_MONTH_DAY_RW = 0x32
        MONTHLY_WATT_R = 0x33
        TIMER_OFF_2_RW = 0x34

    def __init__(self):
        super(AirConditioner, self).__init__()
        self.set_dev_type(DeviceTypeCode.AIR_CONDITIONER)

    @classmethod
    def module_name(cls):
        return __name__


class DevicePowerService(DeviceCommonOnOffService):
    # POWER_RW = 0x00
    pass


class DeviceOpModeService(DeviceEnum16Service):
    # OP_MODE_RW = 0x01
    class ParamCode(BaseObject):
        COOL = 0x00
        DEHUMIDIFIER = 0x01
        FAN = 0x02
        AUTO = 0x03
        HEAT = 0x04


class DeviceFanLevelService(DeviceFeatureLevelService):
    # FAN_LEVEL_RW = 0x02
    pass


class DeviceTemperatureCfgService(DeviceUint8Service):
    # TEMPERATURE_CFG_RW = 0x03
    pass


class DeviceTemperatureRService(DeviceInt8Service):
    # TEMPERATURE_R = 0x04
    pass


class DeviceComfortableService(DeviceCommonOnOffService):
    # COMFORTABLE_RW = 0x05
    pass


class DeviceComfortableTimerService(DeviceUint16Service):
    # COMFORTABLE_TIMER_RW = 0x06
    pass


class DeviceFuzzyTemperatureService(DeviceEnum16Service):
    # FUZZY_TEMPERATURE_RW = 0x07
    class ParamCode(BaseObject):
        JUST_FIT = 0x00
        TOO_COLD = 0x01
        TOO_HOT = 0x02
        OFF = 0x03
        ON = 0x04


class DeviceAirCleanModeService(DeviceCommonOnOffService):
    # AIR_CLEAN_MODE_RW = 0x08
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


class DeviceFanUpdownService(DeviceCommonOnOffService):
    # FAN_UPDOWN_RW = 0x0e
    pass


class DeviceFanUpdownLevelService(DeviceFeatureLevelService):
    # FAN_UPDOWN_LEVEL_RW = 0x0f
    pass


class DeviceFanSwingService(DeviceCommonOnOffService):
    # FAN_SWING_RW = 0x10
    pass


class DeviceFanSwingLevelService(DeviceFeatureLevelService):
    # FAN_SWING_LEVEL_RW = 0x11
    pass


class DeviceFilterCleanNotifyService(DeviceEnum16Service):
    # FILTER_CLEAN_NOTIFY_RW = 0x12
    class ParamCode(BaseObject):
        NORMAL = 0x00
        ABNORMAL = 0x01


class DeviceDehumidifierCfgService(DeviceUint8Service):
    # DEHUMIDIFIER_CFG_RW = 0x13
    pass


class DeviceHumidityRService(DeviceUint8Service):
    # HUMIDITY_R = 0x14
    pass


class DeviceSysCheckRService(DeviceEnum16BitService):
    # SYS_CHECK_R = 0x15
    class ParamCode(BaseObject):
        NORMAL = 0
        ERR_1 = 1
        ERR_2 = 2
        ERR_3 = 3
        ERR_4 = 4
        ERR_5 = 5
        ERR_6 = 6
        ERR_7 = 7
        ERR_8 = 8
        ERR_9 = 9
        ERR_10 = 10
        ERR_11 = 11
        ERR_12 = 12
        ERR_13 = 13
        ERR_14 = 14
        ERR_15 = 15


class DeviceAirDetectService(DeviceCommonOnOffService):
    # AIR_DETECT_RW = 0x16
    pass


class DeviceDevMildewService(DeviceCommonOnOffService):
    # DEV_MILDEW_RW = 0x17
    pass


class DeviceSelfCleanService(DeviceCommonOnOffService):
    # SELF_CLEAN_RW = 0x18
    pass


class DeviceMotionDetectModeService(DeviceEnum16Service):
    # MOTION_DETECT_MODE_RW = 0x19
    class ParamCode(BaseObject):
        OFF = 0
        DETECT_HUMAN = 1
        NOT_DETECT_HUMAN = 2
        AUTO = 3


class DeviceFastOpService(DeviceCommonOnOffService):
    # FAST_OP_RW = 0x1a
    pass


class DevicePowerSavingOpService(DeviceCommonOnOffService):
    # POWER_SAVING_OP_RW = 0x1b
    pass


class DevicePowerLimitOpService(DeviceUint16Service):
    # POWER_LIMIT_OP_RW = 0x1c
    pass


class DeviceRemoteCtrlLockService(DeviceEnum16BitService):
    # REMOTE_CTRL_LOCK_RW = 0x1d
    pass


class DeviceSaaCtrlAudioService(DeviceEnum16Service):
    # SAA_CTRL_AUDIO_RW = 0x1e
    pass


class DeviceBodyDisplayModeService(DeviceEnum16Service):
    # BODY_DISPLAY_MODE_RW = 0x1f
    pass


class DeviceMoisturizeModeService(DeviceEnum16Service):
    # MOISTURIZE_MODE_RW = 0x20
    pass


class DeviceOutdoorTemperatureRService(DeviceEnum16Service):
    # OUTDOOR_TEMPERATURE_R = 0x21
    pass


class DeviceIndoorUnitWattRService(DeviceEnum16Service):
    # INDOOR_UNIT_WATT_R = 0x22
    pass


class DeviceOutdoorUnitWattRService(DeviceEnum16Service):
    # OUTDOOR_UNIT_WATT_R = 0x23
    pass


class DeviceOutdoorUnitCurrentRService(DeviceEnum16Service):
    # OUTDOOR_UNIT_CURRENT_R = 0x24
    pass


class DeviceOutdoorUnitVoltateRService(DeviceEnum16Service):
    # OUTDOOR_UNIT_VOLTATE_R = 0x25
    pass


class DeviceOutdoorUnitPowerFactorRService(DeviceEnum16Service):
    # OUTDOOR_UNIT_POWER_FACTOR_R = 0x26
    pass


class DeviceOutdoorUnitInstantWattRService(DeviceEnum16Service):
    # OUTDOOR_UNIT_INSTANT_WATT_R = 0x27
    pass


class DeviceTotalWattService(DeviceEnum16Service):
    # TOTAL_WATT_RW = 0x28
    pass


class DeviceDisplayErrRService(DeviceEnum16Service):
    # DISPLAY_ERR_R = 0x29
    pass


class DeviceErrHistory1RService(DeviceEnum16BitService):
    # ERR_HISTORY_1_R = 0x2a
    pass


class DeviceErrHistory2RService(DeviceEnum16BitService):
    # ERR_HISTORY_2_R = 0x2b
    pass


class DeviceErrHistory3RService(DeviceEnum16BitService):
    # ERR_HISTORY_3_R = 0x2c
    pass


class DeviceErrHistory4RService(DeviceEnum16BitService):
    # ERR_HISTORY_4_R = 0x2d
    pass


class DeviceErrHistory5RService(DeviceEnum16BitService):
    # ERR_HISTORY_5_R = 0x2e
    pass


class DeviceMaintenanceAccuOpHourService(DeviceEnum16Service):
    # MAINTENANCE_ACCU_OP_HOUR_RW = 0x2f
    pass


class DeviceFilterAccuOpHourService(DeviceEnum16Service):
    # FILTER_ACCU_OP_HOUR_RW = 0x30
    pass


class DeviceSysYearService(DeviceEnum16Service):
    # SYS_YEAR_RW = 0x31
    pass


class DeviceSysMonthDayService(DeviceEnum16Service):
    # SYS_MONTH_DAY_RW = 0x32
    pass


class DeviceMonthlyWattRService(DeviceEnum16Service):
    # MONTHLY_WATT_R = 0x33
    pass


class DeviceTimerOff2Service(DeviceEnum16Service):
    # TIMER_OFF_2_RW = 0x34
    pass


if __name__ == '__main__':
    FORMAT = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    dev_cls = AirConditioner
    # dev_cls.print_service_cls_template()
    dev_obj = dev_cls()
    logger.info('{}'.format(dev_obj.device_detail(cmd_check_serv=False)))
