import enum
import logging
from .devices import SADevice
from .devices import SAEngModeService
from .services import UInt8Service
from .services import Int8Service
from .services import UInt16Service
from .services import Enum16BitService
from .services import SAServiceBase
from .services import Enum16Service
from .services import HMService
from .services import MDService
from .services import SACmdHelp

logger = logging.getLogger(__name__)


class ACPowerService(Enum16Service):
    """電源控制功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACPowerService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACOpModeService(Enum16Service):
    """電源控制功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACOpModeService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '冷氣', 1: '除濕', 2: '送風', 3: '自動', 4: '暖氣'
        })
        return _help


class ACFanLevelService(Enum16Service):
    """風速設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFanLevelService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: 'auto',
            '<int>': '1~15'
        })
        return _help


class ACTemperatureCfgService(UInt8Service):
    """溫度設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACTemperatureCfgService, self).to_cmd_help()
        _help.update_kwargs_unit('C')
        _help.update_kwargs_params({
            '<int>': '設定溫度設定值'
        })
        return _help


class ACTemperatureService(Int8Service):
    """室內溫度顯示功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACTemperatureService, self).to_cmd_help()
        _help.update_kwargs_unit('C')
        return _help


class ACComfortableService(Enum16Service):
    """舒眠模式設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACComfortableService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACComfortableTimerService(UInt16Service):
    """舒眠模式剩餘時間設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACComfortableTimerService, self).to_cmd_help()
        _help.update_kwargs_unit('Min')
        _help.update_kwargs_params({
            '<int>': '舒眠模式剩餘時間設定值'
        })
        return _help


class ACFuzzyTemperatureService(Enum16Service):
    """Fuzzy溫度模式設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFuzzyTemperatureService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '剛好', 1: '太冷', 2: '太熱', 3: '關閉', 4: '開啟'
        })
        return _help


class ACAirCleanModeService(Enum16Service):
    """空氣清淨功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACAirCleanModeService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACClockOnService(HMService):
    """開機時間設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACClockOnService, self).to_cmd_help()
        _help.update_kwargs_unit('Hr/Min')
        _help.update_kwargs_params({
            0: '停止定時開時間設定功能',
            '<hour>,<minute>': '定時開時間設定值(倒數計算)'
        })
        return _help


class ACClockOffService(HMService):
    """關機時間設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACClockOffService, self).to_cmd_help()
        _help.update_kwargs_unit('Hr/Min')
        _help.update_kwargs_params({
            0: '停止定時關時間設定功能',
            '<hour>,<minute>': '定時關時間設定值(倒數計算)'
        })
        return _help


class ACTimerOnService(UInt16Service):
    """定時開機功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACTimerOnService, self).to_cmd_help()
        _help.update_kwargs_unit('Min')
        _help.update_kwargs_params({
            0: '停止定時關時間設定功能', '<int>': '定時關時間設定值(倒數計算)'
        })
        return _help


class ACTimerOffService(UInt16Service):
    """定時關機功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACTimerOffService, self).to_cmd_help()
        _help.update_kwargs_unit('Min')
        _help.update_kwargs_params({
            0: '停止定時關時間設定功能', '<int>': '定時關時間設定值(倒數計算)'
        })
        return _help


class ACSysTimeService(HMService):
    """系統（絕對）時間設定"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACSysTimeService, self).to_cmd_help()
        _help.update_kwargs_params({
            '<hour>,<minute>': '時,分'
        })
        return _help


class ACFanUpdownService(Enum16Service):
    """開關上下吹風自動轉向功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFanUpdownService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACFanUpdownLevelService(Enum16Service):
    """設定上下吹風轉向段數功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFanUpdownLevelService, self).to_cmd_help()
        _help.update_kwargs_unit('段')
        _help.update_kwargs_params({
            '0~15': '0~15段'
        })
        return _help


class ACFanSwingService(Enum16Service):
    """開關左右吹風自動轉向功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFanSwingService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACFanSwingLevelService(Enum16Service):
    """設定左右吹風轉向段數功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFanSwingLevelService, self).to_cmd_help()
        _help.update_kwargs_unit('段')
        _help.update_kwargs_params({
            '0~15': '0~15段'
        })
        return _help


class ACFilterCleanNotifyService(Enum16Service):
    """濾網清洗通知功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFilterCleanNotifyService, self).to_cmd_help()
        _help.update_kwargs_unit('%')
        _help.update_kwargs_params({
            'READ': {0: '正常', 1: '須清洗'}, 'WRITE': {0: '重置狀態'}
        })
        return _help


class ACDehumidifierCfgService(UInt8Service):
    """溼度設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACDehumidifierCfgService, self).to_cmd_help()
        _help.update_kwargs_unit('%')
        _help.update_kwargs_params({
            'n': '設定溼度設定值'
        })
        return _help


class ACHumidityService(UInt8Service):
    """室內溼度顯示功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACHumidityService, self).to_cmd_help()
        _help.update_kwargs_unit('%')
        _help.update_kwargs_params({
            'n': '設定溼度設定值'
        })
        return _help


class ACSysCheckService(Enum16BitService):
    """點檢設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACSysCheckService, self).to_cmd_help()
        return _help


class ACAirDetectService(Enum16Service):
    """空氣偵測控制功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACAirDetectService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACDevMildewService(Enum16Service):
    """防霉控制功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACDevMildewService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACSelfCleanService(Enum16Service):
    """自體淨控制功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACSelfCleanService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACMotionDetectModeService(Enum16Service):
    """動向感應模式設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACMotionDetectModeService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '對人', 2: '不對人', 3: '自動判斷'
        })
        return _help


class ACFastOpService(Enum16Service):
    """快速運轉功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFastOpService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACPowerSavingOpService(Enum16Service):
    """節電運轉功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACPowerSavingOpService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉', 1: '開啟'
        })
        return _help


class ACPowerLimitOpService(UInt16Service):
    """限電模式"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACPowerLimitOpService, self).to_cmd_help()
        _help.update_kwargs_unit('%')
        _help.update_kwargs_params({
            0: '關閉(不限電模式)', '非0': '額定運轉電流百分比'
        })
        return _help


class ACRemoteCtrlLockService(Enum16BitService):
    """有線控制器、無線遙控器禁止功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACRemoteCtrlLockService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '開關', 1: '運轉模式', 2: '溫度設定', 3: '風速', 4: '自動風向板(上下左右)', 5: '停止鍵常時有效'
        })
        return _help


class ACSaaCtrlAudioService(Enum16Service):
    """SAA控制提示音功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACSaaCtrlAudioService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '有聲', 1: '無聲'
        })
        return _help


class ACBodyDisplayModeService(Enum16Service):
    """機體顯示模式設定"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACBodyDisplayModeService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '亮', 1: '暗', 2: '關', 3: '全關'
        })
        return _help


class ACMoisturizeModeService(Enum16Service):
    """保濕模式設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACMoisturizeModeService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '無', 1: '低', 2: '高'
        })
        return _help


class ACOutdoorTemperatureService(Int8Service):
    """室外溫度功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACOutdoorTemperatureService, self).to_cmd_help()
        _help.update_kwargs_unit('C')
        return _help


class ACIndoorUnitWattService(UInt16Service):
    """室內機能力"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACIndoorUnitWattService, self).to_cmd_help()
        _help.update_kwargs_unit('0.1k')
        return _help


class ACOutdoorUnitWattService(UInt16Service):
    """室外機能力"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACOutdoorUnitWattService, self).to_cmd_help()
        _help.update_kwargs_unit('0.1k')
        return _help


class ACOutdoorUnitCurrentService(UInt16Service):
    """室外機運轉電流"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACOutdoorUnitCurrentService, self).to_cmd_help()
        _help.update_kwargs_unit('0.1Amp')
        return _help


class ACOutdoorUnitVoltateService(UInt16Service):
    """室外機運轉電壓"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACOutdoorUnitVoltateService, self).to_cmd_help()
        _help.update_kwargs_unit('V')
        return _help


class ACOutdoorUnitPowerFactorService(UInt16Service):
    """室外機運轉功因"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACOutdoorUnitPowerFactorService, self).to_cmd_help()
        return _help


class ACOutdoorUnitInstantWattService(UInt16Service):
    """室外機即時功率"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACOutdoorUnitInstantWattService, self).to_cmd_help()
        _help.update_kwargs_unit('W')
        return _help


class ACTotalWattService(UInt16Service):
    """室外機累積用電量
    R:目前累積電量,W:0:清除電量累積
    """

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACTotalWattService, self).to_cmd_help()
        _help.update_kwargs_unit('0.1kWh')
        _help.update_kwargs_params({
            0: '清除電量累積'
        })
        return _help


class ACDisplayErrService(Enum16BitService):
    """錯誤訊息顯示功能: 0:正常,非0:故障訊息碼"""
    pass


class ACErrHistory1Service(Enum16BitService):
    """故障履歷1: 0:正常,非0:故障訊息碼"""
    pass


class ACErrHistory2Service(Enum16BitService):
    """故障履歷2: 0:正常,非0:故障訊息碼"""
    pass


class ACErrHistory3Service(Enum16BitService):
    """故障履歷3: 0:正常,非0:故障訊息碼"""
    pass


class ACErrHistory4Service(Enum16BitService):
    """故障履歷4: 0:正常,非0:故障訊息碼"""
    pass


class ACErrHistory5Service(Enum16BitService):
    """故障履歷5: 0:正常,非0:故障訊息碼"""
    pass


class ACMaintenanceAccuOpHourService(UInt16Service):
    """定期保養累積運轉小時功能
    R:讀取目前累計運轉小時數, W:0:重置運轉小時數
    """

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACMaintenanceAccuOpHourService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '重置運轉小時數'
        })
        return _help


class ACFilterAccuOpHourService(UInt16Service):
    """濾網清洗累積運轉小時功能
    R:讀取目前累計運轉小時數, W:0:重置運轉小時數
    """

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACFilterAccuOpHourService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '重置運轉小時數'
        })
        return _help


class ACSysYearService(UInt16Service):
    """系統時間-年設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACSysYearService, self).to_cmd_help()
        _help.update_kwargs_params({
            'year': '顯示/設定 年'
        })
        return _help


class ACSysMonthDayService(MDService):
    """系統時間-月/日設定功能
    電力累計計算用-月/日設定功能，顯示/設定 月/日Byte3代表月、Byte4代表日
    """

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACSysMonthDayService, self).to_cmd_help()
        _help.update_kwargs_params({
            '<month>,<day>': '月,日'
        })
        return _help


class ACMonthlyWattService(UInt16Service):
    """月累積用電量
    R:目前累積電量,下達命令時, Byte4表示1~12月
    """

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACMonthlyWattService, self).to_cmd_help()
        _help.update_kwargs_unit('0.1kWh')
        _help.update_kwargs_params({
            0: '目前累積電量', '1~12': 'Byte4表示1~12月'
        })
        return _help


class ACTimerOff2Service(UInt16Service):
    """定時開關機功能
    定時關機時間(日立定速及窗型機使用)，冷氣於開機狀態時,此功能代表定時關機時間,反之冷氣於關機狀態時,代表定時開機時間
    """

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(ACTimerOff2Service, self).to_cmd_help()
        _help.update_kwargs_unit('Min')
        _help.update_kwargs_params({
            0: '停止定時開關機功能', '非0': '非0之值代表定時開關機時間'
        })
        return _help


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
        elif 0x50 <= _service.service_id <= 0x7E:
            _service = SAEngModeService.from_fixed_len_pdu(pdu=pdu)
        else:
            logger.warning(f'Unknown {cls.__name__} service_id {_service.service_id}')
            _service = SAServiceBase.from_fixed_len_pdu(pdu=pdu)

        _service.name = ACServiceIDEnum(_service.service_id).name
        return _service


__all__ = [
    'ACServiceIDEnum',
    'AirConditioner'
]
