import enum
import logging
from .services import UInt8Service
from .services import Int8Service
from .services import UInt16Service
from .services import HMService
from .services import Enum16BitService
from .services import MDService
from .services import SAServiceBase
from .services import Enum16Service

logger = logging.getLogger(__name__)


class SADevice:

    @classmethod
    def convert_dev_specific_service(cls, pdu: list, is_fixed_len_pdu: bool) -> SAServiceBase:
        raise NotImplementedError


class _PowerService(Enum16Service):
    OFF = 0
    ON = 1

    def to_cmd_help(self):
        _help = super(_PowerService, self).to_cmd_help()
        _help.update({
            'values': {
                ACPowerService.OFF: 'ON',
                ACPowerService.ON: 'OFF'
            }
        })
        return _help


class ACPowerService(_PowerService):
    pass


class ACOpModeService(enum.IntEnum):
    COOL = 0
    DEHUMIDIFICATION = 1
    FAN = 2
    AUTO = 3
    HEAT = 4


class ACFanLevelService(enum.IntEnum):
    AUTO = 0
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


# class ACTemperatureCfgService(enum.IntEnum):
# class ACTemperatureService(enum.IntEnum):
class ACComfortableService(enum.IntEnum):
    OFF = 0
    ON = 1


# class ACComfortableTimerService(enum.IntEnum):
class ACFuzzyTemperatureService(enum.IntEnum):
    BALANCE = 0
    COLD = 1
    HOT = 2
    OFF = 3
    ON = 4


class ACAirCleanModeService(enum.IntEnum):
    OFF = 0
    ON = 1


# class ACClockOnService(enum.IntEnum):
# class ACClockOffService(enum.IntEnum):
# class ACTimerOnService(enum.IntEnum):
# class ACTimerOffService(enum.IntEnum):
# class ACSysTimeService(enum.IntEnum):
class ACFanUpdownService(enum.IntEnum):
    OFF = 0
    ON = 1


class ACFanUpdownLevelService(enum.IntEnum):
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


class ACFanSwingService(enum.IntEnum):
    OFF = 0
    ON = 1


class ACFanSwingLevelService(enum.IntEnum):
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


class ACFilterCleanNotifyService(enum.IntEnum):
    NORMAL = 0
    NEED_CLEAN = 1


# class ACDehumidifierCfgService(enum.IntEnum):
# class ACHumidityService(enum.IntEnum):
class ACSysCheckService(enum.IntEnum):
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


class ACAirDetectService(enum.IntEnum):
    OFF = 0
    ON = 1


class ACDevMildewService(enum.IntEnum):
    OFF = 0
    ON = 1


class ACSelfCleanService(enum.IntEnum):
    OFF = 0
    ON = 1


class ACMotionDetectModeService(enum.IntEnum):
    OFF = 0
    DETECT_PERSON = 1
    NOT_DETECT_PERSON = 2
    AUTO_DETECTION = 3


class ACFastOpService(enum.IntEnum):
    OFF = 0
    ON = 1


class ACPowerSavingOpService(enum.IntEnum):
    OFF = 0
    ON = 1


# class ACPowerLimitOpService(enum.IntEnum):
class ACRemoteCtrlLockService(enum.IntEnum):
    POWER = 0
    OP_MODE = 1
    TEMPERATURE_CFG = 2
    FAN_UP_DOWN = 3
    FAN_UPDOWN_SWING = 4
    OFF_KEY = 5


class ACSaaCtrlAudioService(enum.IntEnum):
    AUDIO = 0
    SILENT = 1


class ACBodyDisplayModeService(enum.IntEnum):
    BRIGHT = 0
    DARK = 1
    OFF = 2
    ALL_OFF = 3


class ACMoisturizeModeService(enum.IntEnum):
    OFF = 0
    LOW = 1
    HIGH = 2


# class ACOutdoorTemperatureService(enum.IntEnum):
# class ACIndoorUnitWattService(enum.IntEnum):
# class ACOutdoorUnitWattService(enum.IntEnum):
# class ACOutdoorUnitCurrentService(enum.IntEnum):
# class ACOutdoorUnitVoltateService(enum.IntEnum):
# class ACOutdoorUnitPowerFactorService(enum.IntEnum):
# class ACOutdoorUnitInstantWattService(enum.IntEnum):
# class ACTotalWattService(enum.IntEnum):
class ACDisplayErrService(enum.IntEnum):
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


class ACErrHistory1Service(enum.IntEnum):
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


class ACErrHistory2Service(enum.IntEnum):
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


class ACErrHistory3Service(enum.IntEnum):
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


class ACErrHistory4Service(enum.IntEnum):
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


class ACErrHistory5Service(enum.IntEnum):
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


# class ACMaintenanceAccuOpHourService(enum.IntEnum):
# class ACFilterAccuOpHourService(enum.IntEnum):
# class ACSysYearService(enum.IntEnum):
# class ACSysMonthDayService(enum.IntEnum):
# class ACMonthlyWattService(enum.IntEnum):
# class ACTimerOff2Service(enum.IntEnum):


class ACServiceIDEnum(enum.IntEnum):
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


class AirConditioner(SADevice):
    @classmethod
    def convert_dev_specific_service(cls, pdu: list, is_fixed_len_pdu: bool) -> SAServiceBase:
        if not isinstance(pdu, list) or len(pdu) < 3:
            raise ValueError(f'service pdu invalid, {pdu}')
        if not is_fixed_len_pdu:
            raise NotImplementedError

        _pdu = list(pdu)
        logger.debug(f'parsing dev service pdu {_pdu}')
        _service = SAServiceBase.from_fixed_len_pdu(pdu=_pdu)
        if _service.service_id == ACServiceIDEnum.POWER_RW:
            _service = ACPowerService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.OP_MODE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FAN_LEVEL_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.TEMPERATURE_CFG_RW:
            _service = UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.TEMPERATURE_R:
            _service = Int8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.COMFORTABLE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.COMFORTABLE_TIMER_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FUZZY_TEMPERATURE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.AIR_CLEAN_MODE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.CLOCK_ON_RW:
            _service = HMService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.CLOCK_OFF_RW:
            _service = HMService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.TIMER_ON_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.TIMER_OFF_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.SYS_TIME_RW:
            _service = HMService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FAN_UPDOWN_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FAN_UPDOWN_LEVEL_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FAN_SWING_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FAN_SWING_LEVEL_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FILTER_CLEAN_NOTIFY_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.DEHUMIDIFIER_CFG_RW:
            _service = UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.HUMIDITY_R:
            _service = UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.SYS_CHECK_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.AIR_DETECT_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.DEV_MILDEW_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.SELF_CLEAN_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.MOTION_DETECT_MODE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FAST_OP_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.POWER_SAVING_OP_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.POWER_LIMIT_OP_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.REMOTE_CTRL_LOCK_RW:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.SAA_CTRL_AUDIO_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.BODY_DISPLAY_MODE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.MOISTURIZE_MODE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.OUTDOOR_TEMPERATURE_R:
            _service = Int8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.INDOOR_UNIT_WATT_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.OUTDOOR_UNIT_WATT_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.OUTDOOR_UNIT_CURRENT_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.OUTDOOR_UNIT_VOLTATE_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.OUTDOOR_UNIT_POWER_FACTOR_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.OUTDOOR_UNIT_INSTANT_WATT_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.TOTAL_WATT_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.DISPLAY_ERR_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.ERR_HISTORY_1_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.ERR_HISTORY_2_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.ERR_HISTORY_3_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.ERR_HISTORY_4_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.ERR_HISTORY_5_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.MAINTENANCE_ACCU_OP_HOUR_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.FILTER_ACCU_OP_HOUR_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.SYS_YEAR_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.SYS_MONTH_DAY_RW:
            _service = MDService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.MONTHLY_WATT_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == ACServiceIDEnum.TIMER_OFF_2_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        else:
            logger.warning(f'Unknown {cls.__name__} service_id {_service.service_id}')
            _service = Enum16Service.from_fixed_len_pdu(pdu=pdu)

        _service.name = ACServiceIDEnum(_service.service_id).name
        return _service


class DehumidifierServiceIDEnum(enum.IntEnum):
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


class DHPowerService(_PowerService):
    pass


class Dehumidifier(SADevice):
    @classmethod
    def convert_dev_specific_service(cls, pdu: list, is_fixed_len_pdu: bool) -> SAServiceBase:
        if not isinstance(pdu, list) or len(pdu) < 3:
            raise ValueError(f'service pdu invalid, {pdu}')
        if not is_fixed_len_pdu:
            raise NotImplementedError

        _pdu = list(pdu)
        _service = SAServiceBase.from_fixed_len_pdu(pdu=_pdu)
        if _service.service_id == DehumidifierServiceIDEnum.POWER_RW:
            _service = DHPowerService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.OP_MODE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.OP_TIMER_RW:
            _service = UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.HUMIDITY_CFG_RW:
            _service = UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.DEHUMIDIFIER_LEVEL_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.DRY_CLOTHE_LEVEL_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.TEMPERATURE_R:
            _service = Int8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.HUMIDITY_R:
            _service = UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.FAN_DIRECTION_AUTO_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.FAN_DIRECTION_LEVEL_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.WATER_FULL_ALARM_R:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.FILTER_CLEAN_NOTIFY_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.MOOD_LED_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.AIR_CLEAN_MODE_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.FAN_LEVEL_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.SIDE_FAN_R:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.AUDIO_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.DEFROST_DISPLAY_R:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.DISPLAY_ERR_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.DEV_MILDEW_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.HUMIDITY_HIGH_NOTIFY_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.HUMIDITY_HIGH_CFG_RW:
            _service = UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.KEYPAD_LOCK_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.REMOTE_CTRL_LOCK_RW:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.SAA_CTRL_AUDIO_RW:
            _service = Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.OP_CURRENT_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.OP_VOLTAGE_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.OP_POWER_FACTOR_R:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.OP_POWER_WATT_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.TOTAL_WATT_RW:
            _service = UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.ERR_HISTORY_1_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.ERR_HISTORY_2_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.ERR_HISTORY_3_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.ERR_HISTORY_4_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DehumidifierServiceIDEnum.ERR_HISTORY_5_R:
            _service = Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        else:
            raise NotImplementedError

        _service.name = ACServiceIDEnum(_service.service_id).name
        return _service


__all__ = [
    'AirConditioner',
    'ACServiceIDEnum',
    'Dehumidifier',
    'DehumidifierServiceIDEnum'
]
