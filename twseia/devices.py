import enum
from .services import UInt8Service, SADataValueType, Int8Service, UInt16Service, HMService, Enum16BitService, MDService
from .services import ServiceBase
from .services import Enum16Service


class _DeviceBase:
    @classmethod
    def convert_dev_specific_service(cls, pud: list, is_fixed_len_pdu: bool) -> ServiceBase:
        raise NotImplementedError


class SADevice:

    @classmethod
    def convert_services_from_pdu(cls, pdu: list, is_fixed_len_pdu: bool) -> list:
        raise NotImplementedError


class AirConditionerServiceIDEnum(enum.IntEnum):
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


class AirConditioner(_DeviceBase, SADevice):
    @classmethod
    def convert_dev_specific_service(cls, pdu: list, is_fixed_len_pdu: bool) -> ServiceBase:
        assert (isinstance(pdu, list) and len(pdu) == 3)
        _pdu = list(pdu)
        if not is_fixed_len_pdu:
            raise NotImplementedError
        _service = ServiceBase.from_fixed_len_pdu(pdu=_pdu)
        if _service.service_id == AirConditionerServiceIDEnum.POWER_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.OP_MODE_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FAN_LEVEL_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.TEMPERATURE_CFG_RW:
            return UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.TEMPERATURE_R:
            return Int8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.COMFORTABLE_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.COMFORTABLE_TIMER_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FUZZY_TEMPERATURE_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.AIR_CLEAN_MODE_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.CLOCK_ON_RW:
            return HMService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.CLOCK_OFF_RW:
            return HMService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.TIMER_ON_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.TIMER_OFF_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.SYS_TIME_RW:
            return HMService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FAN_UPDOWN_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FAN_UPDOWN_LEVEL_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FAN_SWING_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FAN_SWING_LEVEL_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FILTER_CLEAN_NOTIFY_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.DEHUMIDIFIER_CFG_RW:
            return UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.HUMIDITY_R:
            return UInt8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.SYS_CHECK_R:
            return Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.AIR_DETECT_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.DEV_MILDEW_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.SELF_CLEAN_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.MOTION_DETECT_MODE_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FAST_OP_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.POWER_SAVING_OP_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.POWER_LIMIT_OP_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.REMOTE_CTRL_LOCK_RW:
            return Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.SAA_CTRL_AUDIO_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.BODY_DISPLAY_MODE_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.MOISTURIZE_MODE_RW:
            return Enum16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.OUTDOOR_TEMPERATURE_R:
            return Int8Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.INDOOR_UNIT_WATT_R:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.OUTDOOR_UNIT_WATT_R:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.OUTDOOR_UNIT_CURRENT_R:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.OUTDOOR_UNIT_VOLTATE_R:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.OUTDOOR_UNIT_POWER_FACTOR_R:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.OUTDOOR_UNIT_INSTANT_WATT_R:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.TOTAL_WATT_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.DISPLAY_ERR_R:
            return Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.ERR_HISTORY_1_R:
            return Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.ERR_HISTORY_2_R:
            return Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.ERR_HISTORY_3_R:
            return Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.ERR_HISTORY_4_R:
            return Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.ERR_HISTORY_5_R:
            return Enum16BitService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.MAINTENANCE_ACCU_OP_HOUR_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.FILTER_ACCU_OP_HOUR_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.SYS_YEAR_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.SYS_MONTH_DAY_RW:
            return MDService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.MONTHLY_WATT_R:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == AirConditionerServiceIDEnum.TIMER_OFF_2_RW:
            return UInt16Service.from_fixed_len_pdu(pdu=_pdu)
        else:
            raise Exception(f'Unknown device {cls.__name__} service_id {_service.service_id}')

    @classmethod
    def convert_services_from_pdu(cls, pdu: list, is_fixed_len_pdu: bool) -> list:
        if not isinstance(pdu, list):
            raise ValueError(f'pdu type invalid, {pdu}')
        _pdu = list(pdu)
        services = []
        n = 0
        while n < len(pdu):
            if is_fixed_len_pdu:
                _len = 3
            else:
                data_type_id = _pdu[n+1]
                _len = SADataValueType.read_data_type_len_by_id(data_type_id=data_type_id)

            service = cls.convert_dev_specific_service(
                pdu=pdu[n:n + _len],
                is_fixed_len_pdu=is_fixed_len_pdu
            )
            services.append(service)
            n += _len
        return services
