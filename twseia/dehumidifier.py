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
from .services import SACmdHelp

logger = logging.getLogger(__name__)


class DHPowerService(Enum16Service):
    """電源控制功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(DHPowerService, self).to_cmd_help()
        _help.update_kwargs_params(value={
            0: '關閉電源', 1: '開啟電源'
        })
        return _help


class DHOpModeService(Enum16Service):
    """運轉模式設定功能"""

    def to_cmd_help(self) -> SACmdHelp:
        _help = super(DHOpModeService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '自動除濕',
            1: '設定除濕',
            2: '連續除濕',
            3: '乾衣',
            4: '空氣清淨',
            5: '防霉防蟎',
            6: '送風',
            7: '人體舒適',
            8: '低濕乾燥'
        })
        return _help


class DHOpTimerService(UInt8Service):
    """運轉時間設定功能"""
    unit = 'Hr'

    def to_cmd_help(self):
        _help = super(DHOpTimerService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉設定時間功能',
            '非0': '代表運轉時間'
        })
        _help.update_kwargs_unit('Hr')
        return _help


class DHHumidityCfgService(UInt8Service):
    """相對溼度設定功能"""
    unit = '%'

    def to_cmd_help(self):
        _help = super(DHHumidityCfgService, self).to_cmd_help()
        _help.update_kwargs_params({
            '非0': '相對溼度設定值（百分比）'
        })
        _help.update_kwargs_unit('%')
        return _help


class DHDehumidifierLevelService(Enum16Service):
    """除濕段數設定功能"""

    def to_cmd_help(self):
        _help = super(DHDehumidifierLevelService, self).to_cmd_help()
        _help.update_kwargs_params({
            '0~15': 'n段除濕(0~15段數愈高相對濕度愈高)'
        })
        return _help


class DHDryClotheLevelService(Enum16Service):
    """乾衣段數設定功能"""

    def to_cmd_help(self):
        _help = super(DHDryClotheLevelService, self).to_cmd_help()
        _help.update_kwargs_params({
            '0~15': 'n段乾衣'
        })
        return _help


class DHTemperatureService(Int8Service):
    """室內溫度顯示功能, read only"""
    unit = 'ºC'

    def to_cmd_help(self):
        _help = super(DHTemperatureService, self).to_cmd_help()
        _help.update_kwargs_unit('C')
        return _help


class DHHumidityService(UInt8Service):
    """室內溼度顯示功能, read only"""
    unit = '%'

    def to_cmd_help(self):
        _help = super(DHHumidityService, self).to_cmd_help()
        _help.update_kwargs_unit('%')
        return _help


class DHFanDirectionAutoService(Enum16Service):
    """開關自動風向功能"""

    def to_cmd_help(self):
        _help = super(DHFanDirectionAutoService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '停止', 1: '開啟'
        })
        return _help


class DHFanDirectionLevelService(Enum16Service):
    """設定風向段數功能"""

    def to_cmd_help(self):
        _help = super(DHFanDirectionLevelService, self).to_cmd_help()
        _help.update_kwargs_params({
            '0~15': 'n段角度'
        })
        return _help


class DHWaterFullAlarmService(Enum16Service):
    """滿水顯示警告功能"""

    def to_cmd_help(self):
        _help = super(DHWaterFullAlarmService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '正常狀態', 1: '滿水狀態'
        })
        return _help


class DHFilterCleanNotifyService(Enum16Service):
    """濾網清洗通知功能"""

    def to_cmd_help(self):
        _help = super(DHFilterCleanNotifyService, self).to_cmd_help()
        _help.update_kwargs_params({
            'READ': {0: '正常', 1: '需清洗髒污'}, 'WRITE': {0: '狀態重置'}
        })
        return _help


class DHMoodLedService(Enum16Service):
    """氣氛燈控制功能"""

    def to_cmd_help(self):
        _help = super(DHMoodLedService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉氣氛燈', 1: '開啟氣氛燈'
        })
        return _help


class DHAirCleanModeService(Enum16Service):
    """空氣清淨模式設定功能"""

    def to_cmd_help(self):
        _help = super(DHAirCleanModeService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉空氣清淨功能', 1: '開啟空氣清淨功能或段數1', 'n': 'n段'
        })
        return _help


class DHFanLevelService(Enum16Service):
    """風速設定功能"""

    def to_cmd_help(self):
        _help = super(DHFanLevelService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '自動', 'n': 'n段風速(1~15段數愈高風速愈強)'
        })
        return _help


class DHSideFanService(Enum16Service):
    """側向出風口功能"""

    def to_cmd_help(self):
        _help = super(DHSideFanService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '正常狀態(上側出風)', 1: '側向出風狀態'
        })
        return _help


class DHAudioService(Enum16Service):
    """聲音設定功能"""

    def to_cmd_help(self):
        _help = super(DHAudioService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '靜音', 1: '按鍵聲音', 2: '滿水及按鍵聲音'
        })
        return _help


class DHDefrostDisplayService(Enum16Service):
    """除霜顯示功能"""

    def to_cmd_help(self):
        _help = super(DHDefrostDisplayService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '正常狀態', 1: '除霜狀態'
        })
        return _help


class DHDisplayErrService(Enum16BitService):
    """錯誤訊息顯示功能"""

    def to_cmd_help(self):
        _help = super(DHDisplayErrService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '正常', '非0': '故障訊息碼'
        })
        return _help


class DHDevMildewService(Enum16Service):
    """機體防霉功能"""

    def to_cmd_help(self):
        _help = super(DHDevMildewService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉機體防霉功能', 1: '開啟機體防霉功能'
        })
        return _help


class DHHumidityHighNotifyService(Enum16Service):
    """高濕度提示設定功能"""

    def to_cmd_help(self):
        _help = super(DHHumidityHighNotifyService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉高濕度提示功能', 1: '開啟高濕度提示功能'
        })
        return _help


class DHHumidityHighCfgService(UInt16Service):
    """高濕度值定義設定功能"""
    unit = '%'

    def to_cmd_help(self):
        _help = super(DHHumidityHighCfgService, self).to_cmd_help()
        _help.update_kwargs_params({
            '0~99': '高濕度提示設定值'
        })
        _help.update_kwargs_unit('%')
        return _help


class DHKeypadLockService(Enum16Service):
    """按鍵鎖功能"""

    def to_cmd_help(self):
        _help = super(DHKeypadLockService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '關閉按鍵鎖定', 1: '開啟按鍵鎖定'
        })
        return _help


class DHRemoteCtrlLockService(Enum16BitService):
    """有線控制器、無線遙控器禁止功能"""

    def to_cmd_help(self):
        _help = super(DHRemoteCtrlLockService, self).to_cmd_help()
        _help.update_kwargs_params({
            'BIT 0': '運轉/停止',
            'BIT 1': '運轉模式',
            'BIT 2': '溼度設定',
            'BIT 3': '風速設定',
            'BIT 4': '自動轉向設定',
            'BIT 5': '停止鍵常時有效',
            'note': '(0是許可,1是禁止)'
        })
        return _help


class DHSaaCtrlAudioService(Enum16Service):
    """SAA控制提示音功能"""

    def to_cmd_help(self):
        _help = super(DHSaaCtrlAudioService, self).to_cmd_help()
        _help.update_kwargs_params({
            0: '有聲', 1: '無聲'
        })
        return _help


class DHOpCurrentService(Enum16Service):
    """運轉電流"""
    unit = '0.1Amp'

    def to_cmd_help(self):
        _help = super(DHOpCurrentService, self).to_cmd_help()
        _help.update_kwargs_unit('0.1Amp')
        return _help


class DHOpVoltageService(UInt16Service):
    """運轉電壓"""
    unit = 'V'

    def to_cmd_help(self):
        _help = super(DHOpVoltageService, self).to_cmd_help()
        _help.update_kwargs_unit('V')
        return _help


class DHOpPowerFactorService(UInt16Service):
    """運轉功因"""
    pass


class DHOpPowerWattService(UInt16Service):
    """即時功率"""
    unit = 'W'

    def to_cmd_help(self):
        _help = super(DHOpPowerWattService, self).to_cmd_help()
        _help.update_kwargs_unit('W')
        return _help


class DHTotalWattService(UInt16Service):
    """累積用電量"""
    unit = '0.1kWh'

    def to_cmd_help(self):
        _help = super(DHTotalWattService, self).to_cmd_help()
        _help.update_kwargs_unit('0.1kWh')
        _help.update_kwargs_params({
            'READ': '目前累積電量', 'WRITE': {0: '清除電量累積'}
        })
        return _help


class DHErrHistory1Service(Enum16BitService):
    """故障履歷1"""
    pass


class DHErrHistory2Service(Enum16BitService):
    """故障履歷2"""
    pass


class DHErrHistory3Service(Enum16BitService):
    """故障履歷3"""
    pass


class DHErrHistory4Service(Enum16BitService):
    """故障履歷4"""
    pass


class DHErrHistory5Service(Enum16BitService):
    """故障履歷5"""
    pass


class DHServiceIDEnum(enum.IntEnum):
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


class Dehumidifier(SADevice):
    @classmethod
    def convert_dev_specific_service(cls, pdu: list, is_fixed_len_pdu: bool = True) -> SAServiceBase:
        if not isinstance(pdu, list) or len(pdu) < 3:
            raise ValueError(f'service pdu invalid, {pdu}')
        if not is_fixed_len_pdu:
            raise NotImplementedError

        _pdu = list(pdu)
        _service = SAServiceBase.from_fixed_len_pdu(pdu=_pdu)
        if _service.service_id == DHServiceIDEnum.POWER_RW:
            _service = DHPowerService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.OP_MODE_RW:
            _service = DHOpModeService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.OP_TIMER_RW:
            _service = DHOpTimerService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.HUMIDITY_CFG_RW:
            _service = DHHumidityCfgService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.DEHUMIDIFIER_LEVEL_RW:
            _service = DHDehumidifierLevelService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.DRY_CLOTHE_LEVEL_RW:
            _service = DHDryClotheLevelService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.TEMPERATURE_R:
            _service = DHTemperatureService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.HUMIDITY_R:
            _service = DHHumidityService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.FAN_DIRECTION_AUTO_RW:
            _service = DHFanDirectionAutoService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.FAN_DIRECTION_LEVEL_RW:
            _service = DHFanDirectionLevelService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.WATER_FULL_ALARM_R:
            _service = DHWaterFullAlarmService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.FILTER_CLEAN_NOTIFY_RW:
            _service = DHFilterCleanNotifyService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.MOOD_LED_RW:
            _service = DHMoodLedService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.AIR_CLEAN_MODE_RW:
            _service = DHAirCleanModeService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.FAN_LEVEL_RW:
            _service = DHFanLevelService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.SIDE_FAN_R:
            _service = DHSideFanService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.AUDIO_RW:
            _service = DHAudioService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.DEFROST_DISPLAY_R:
            _service = DHDefrostDisplayService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.DISPLAY_ERR_R:
            _service = DHDisplayErrService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.DEV_MILDEW_RW:
            _service = DHDevMildewService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.HUMIDITY_HIGH_NOTIFY_RW:
            _service = DHHumidityHighNotifyService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.HUMIDITY_HIGH_CFG_RW:
            _service = DHHumidityHighCfgService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.KEYPAD_LOCK_RW:
            _service = DHKeypadLockService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.REMOTE_CTRL_LOCK_RW:
            _service = DHRemoteCtrlLockService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.SAA_CTRL_AUDIO_RW:
            _service = DHSaaCtrlAudioService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.OP_CURRENT_R:
            _service = DHOpCurrentService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.OP_VOLTAGE_R:
            _service = DHOpVoltageService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.OP_POWER_FACTOR_R:
            _service = DHOpPowerFactorService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.OP_POWER_WATT_RW:
            _service = DHOpPowerWattService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.TOTAL_WATT_RW:
            _service = DHTotalWattService.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.ERR_HISTORY_1_R:
            _service = DHErrHistory1Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.ERR_HISTORY_2_R:
            _service = DHErrHistory2Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.ERR_HISTORY_3_R:
            _service = DHErrHistory3Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.ERR_HISTORY_4_R:
            _service = DHErrHistory4Service.from_fixed_len_pdu(pdu=_pdu)
        elif _service.service_id == DHServiceIDEnum.ERR_HISTORY_5_R:
            _service = DHErrHistory5Service.from_fixed_len_pdu(pdu=_pdu)
        elif 0x50 <= _service.service_id <= 0x7E:
            _service = SAEngModeService.from_fixed_len_pdu(pdu=pdu)
        else:
            logger.warning(f'Unknown {cls.__name__} service_id {_service.service_id}')
            _service = SAServiceBase.from_fixed_len_pdu(pdu=pdu)

        # _service.name = DHServiceIDEnum(_service.service_id).name
        return _service


__all__ = [
    'Dehumidifier',
    'DHServiceIDEnum'
]
