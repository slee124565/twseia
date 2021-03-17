"""
['000000002f326cca', '0000000044a205cd', '000000004797cc32', '000000005b230e9c', '000000007b147fd0', '0000000095e7711e',
'0000000098540bb0', '000000009b7a4dfe', '00000000a11cc647', '00000000b73157bb', '00000000c0efb57f', '00000000c98b737e',
'00000000c9abc6ad', '00000000c9d8e104', '00000000dcba45a1', '00000000de1d380b', '00000000e6a6011d', '00000000ec933f39',
'00000000ec950773', '00000000f834fcbc', '00000000fa5b37ec', '00000000ff5dbd33']
"""

# 0000000044a205cd
kHITACHI_AC_RAS_50NF_REGISTER_PDU = [104, 0, 0, 4, 0, 3, 0, 1, 72, 73, 84, 65, 67, 72, 73, 0, 82, 65, 83, 45, 53, 48,
                                     78, 70, 0, 128, 0, 3, 129, 0, 31, 130, 0, 31, 131, 16, 32, 4, 0, 40, 134, 5, 160,
                                     139, 5, 160, 140, 5, 160, 142, 0, 3, 145, 0, 63, 20, 30, 90, 151, 0, 3, 154, 0, 3,
                                     155, 0, 3, 157, 0, 63, 158, 0, 3, 159, 0, 15, 160, 0, 7, 33, 233, 40, 168, 255,
                                     255, 41, 0, 85, 175, 82, 88, 176, 3, 32, 185, 0, 3, 58, 0, 3, 59, 0, 7, 48]
kHITACHI_AC_RAS_50NF_REGISTER_META = {
    "device": "AirConditioner",
    "services": [
        "0x00: DevicePowerService(code 0x00, RW, min 0, max 3)",
        "0x01: DeviceOpModeService(code 0x01, RW, min 0, max 31)",
        "0x02: DeviceFanLevelService(code 0x02, RW, min 0, max 31)",
        "0x03: DeviceTemperatureCfgService(code 0x03, RW, min 16, max 32)",
        "0x04: DeviceTemperatureRService(code 0x04, R, min 0, max 40)",
        "0x06: DeviceComfortableTimerService(code 0x06, RW, min 5, max 160)",
        "0x0b: DeviceTimerOnService(code 0x0b, RW, min 5, max 160)",
        "0x0c: DeviceTimerOffService(code 0x0c, RW, min 5, max 160)",
        "0x0e: DeviceFanUpdownService(code 0x0e, RW, min 0, max 3)",
        "0x11: DeviceFanSwingLevelService(code 0x11, RW, min 0, max 63)",
        "0x14: DeviceHumidityRService(code 0x14, R, min 30, max 90)",
        "0x17: DeviceDevMildewService(code 0x17, RW, min 0, max 3)",
        "0x1a: DeviceFastOpService(code 0x1a, RW, min 0, max 3)",
        "0x1b: DevicePowerSavingOpService(code 0x1b, RW, min 0, max 3)",
        "0x1d: DeviceRemoteCtrlLockService(code 0x1d, RW, min 0, max 63)",
        "0x1e: DeviceSaaCtrlAudioService(code 0x1e, RW, min 0, max 3)",
        "0x1f: DeviceBodyDisplayModeService(code 0x1f, RW, min 0, max 15)",
        "0x20: DeviceMoisturizeModeService(code 0x20, RW, min 0, max 7)",
        "0x21: DeviceOutdoorTemperatureRService(code 0x21, R, min 233, max 40)",
        "0x28: DeviceTotalWattService(code 0x28, RW, min 255, max 255)",
        "0x29: DeviceDisplayErrRService(code 0x29, R, min 0, max 85)",
        "0x2f: DeviceMaintenanceAccuOpHourService(code 0x2f, RW, min 82, max 88)",
        "0x30: DeviceFilterAccuOpHourService(code 0x30, RW, min 3, max 32)"
    ],
    "brand": "HITACHI",
    "model": "RAS-50NF",
    "cmds": [
        "0x00: power                      DevicePowerService",
        "0x01: op_mode                    DeviceOpModeService",
        "0x02: fan_level                  DeviceFanLevelService",
        "0x03: temperature_cfg            DeviceTemperatureCfgService",
        "0x04: temperature                DeviceTemperatureRService",
        "0x06: comfortable_timer          DeviceComfortableTimerService",
        "0x0b: timer_on                   DeviceTimerOnService",
        "0x0c: timer_off                  DeviceTimerOffService",
        "0x0e: fan_updown                 DeviceFanUpdownService",
        "0x11: fan_swing_level            DeviceFanSwingLevelService",
        "0x14: humidity                   DeviceHumidityRService",
        "0x17: dev_mildew                 DeviceDevMildewService",
        "0x1a: fast_op                    DeviceFastOpService",
        "0x1b: power_saving_op            DevicePowerSavingOpService",
        "0x1d: remote_ctrl_lock           DeviceRemoteCtrlLockService",
        "0x1e: saa_ctrl_audio             DeviceSaaCtrlAudioService",
        "0x1f: body_display_mode          DeviceBodyDisplayModeService",
        "0x20: moisturize_mode            DeviceMoisturizeModeService",
        "0x21: outdoor_temperature        DeviceOutdoorTemperatureRService",
        "0x28: total_watt                 DeviceTotalWattService",
        "0x29: display_err                DeviceDisplayErrRService",
        "0x2f: maintenance_accu_op_hour   DeviceMaintenanceAccuOpHourService",
        "0x30: filter_accu_op_hour        DeviceFilterAccuOpHourService"
    ]
}

kHITACHI_AC_RAD_50NK_REGISTER_PDU = [80, 0, 0, 4, 0, 3, 0, 1, 72, 73, 84, 65, 67, 72, 73, 0, 82, 65, 68, 45, 53,
                                     48, 78, 75, 0, 128, 0, 3, 129, 0, 31, 130, 0, 31, 131, 16, 32, 4, 0, 40, 134,
                                     5, 160, 139, 5, 160, 140, 5, 160, 151, 0, 3, 154, 0, 3, 155, 0, 3, 157, 0, 63,
                                     158, 0, 3, 33, 233, 40, 168, 255, 255, 41, 0, 85, 175, 82, 88, 176, 3, 32,
                                     233]
kHITACHI_AC_RAD_50NK_REGISTER_META = {
    "device": "AirConditioner",
    "services": [
        "0x00: DevicePowerService(code 0x00, RW, min 0, max 3)",
        "0x01: DeviceOpModeService(code 0x01, RW, min 0, max 31)",
        "0x02: DeviceFanLevelService(code 0x02, RW, min 0, max 31)",
        "0x03: DeviceTemperatureCfgService(code 0x03, RW, min 16, max 32)",
        "0x04: DeviceTemperatureRService(code 0x04, R, min 0, max 40)",
        "0x06: DeviceComfortableTimerService(code 0x06, RW, min 5, max 160)",
        "0x0b: DeviceTimerOnService(code 0x0b, RW, min 5, max 160)",
        "0x0c: DeviceTimerOffService(code 0x0c, RW, min 5, max 160)",
        "0x17: DeviceDevMildewService(code 0x17, RW, min 0, max 3)",
        "0x1a: DeviceFastOpService(code 0x1a, RW, min 0, max 3)",
        "0x1b: DevicePowerSavingOpService(code 0x1b, RW, min 0, max 3)",
        "0x1d: DeviceRemoteCtrlLockService(code 0x1d, RW, min 0, max 63)",
        "0x1e: DeviceSaaCtrlAudioService(code 0x1e, RW, min 0, max 3)",
        "0x21: DeviceOutdoorTemperatureRService(code 0x21, R, min 233, max 40)",
        "0x28: DeviceTotalWattService(code 0x28, RW, min 255, max 255)",
        "0x29: DeviceDisplayErrRService(code 0x29, R, min 0, max 85)",
        "0x2f: DeviceMaintenanceAccuOpHourService(code 0x2f, RW, min 82, max 88)",
        "0x30: DeviceFilterAccuOpHourService(code 0x30, RW, min 3, max 32)"
    ],
    "brand": "HITACHI",
    "model": "RAD-50NK",
    "cmds": [
        "0x00: power                      DevicePowerService",
        "0x01: op_mode                    DeviceOpModeService",
        "0x02: fan_level                  DeviceFanLevelService",
        "0x03: temperature_cfg            DeviceTemperatureCfgService",
        "0x04: temperature                DeviceTemperatureRService",
        "0x06: comfortable_timer          DeviceComfortableTimerService",
        "0x0b: timer_on                   DeviceTimerOnService",
        "0x0c: timer_off                  DeviceTimerOffService",
        "0x17: dev_mildew                 DeviceDevMildewService",
        "0x1a: fast_op                    DeviceFastOpService",
        "0x1b: power_saving_op            DevicePowerSavingOpService",
        "0x1d: remote_ctrl_lock           DeviceRemoteCtrlLockService",
        "0x1e: saa_ctrl_audio             DeviceSaaCtrlAudioService",
        "0x21: outdoor_temperature        DeviceOutdoorTemperatureRService",
        "0x28: total_watt                 DeviceTotalWattService",
        "0x29: display_err                DeviceDisplayErrRService",
        "0x2f: maintenance_accu_op_hour   DeviceMaintenanceAccuOpHourService",
        "0x30: filter_accu_op_hour        DeviceFilterAccuOpHourService"
    ]
}

# 000000002f326cca
kPANASONIC_FYTW_08810115_REGISTER_PDU = [69, 0, 0, 4, 0, 3, 0, 4, 80, 97, 110, 97, 115, 111, 110, 105, 99, 0, 70, 89,
                                         84, 87, 45, 48, 56, 56, 49, 48, 49, 49, 53, 0, 128, 0, 3, 129, 0, 127, 130, 0,
                                         12, 132, 0, 6, 7, 0, 0, 137, 0, 15, 10, 0, 0, 141, 0, 3, 142, 0, 15, 18, 0, 0,
                                         152, 0, 3, 157, 0, 0, 212]
kPANASONIC_FYTW_08810115_READ_CLASS_ID_PDU = [6, 0, 1, 0, 0, 7]
kPANASONIC_FYTW_08810115_READ_VERSION_PDU = [6, 0, 2, 4, 0, 0]
kPANASONIC_FYTW_08810115_READ_DEV_TYPE_PDU = [6, 0, 4, 0, 4, 6]
kPANASONIC_FYTW_08810115_READ_BRAND_PDU = [14, 0, 5, 80, 97, 110, 97, 115, 111, 110, 105, 99, 0, 77]
kPANASONIC_FYTW_08810115_READ_MODEL_PDU = [18, 0, 6, 70, 89, 84, 87, 45, 48, 53, 55, 54, 48, 49, 50, 49, 0, 35]
kPANASONIC_FYTW_08810115_SERVICES_PDU = [40, 0, 7, 128, 0, 3, 129, 0, 127, 130, 0, 12, 132, 0, 6, 7, 0, 0, 137, 0, 15, 10, 0, 0, 141, 0, 3, 142, 0, 15, 18, 0, 0, 152, 0, 3, 157, 0, 0, 206]
kPANASONIC_FYTW_08810115_ALL_STATES_PDU = [40, 0, 8, 0, 0, 0, 1, 0, 0, 2, 0, 0, 4, 0, 0, 7, 0, 55, 9, 0, 0, 10, 0, 0, 13, 0, 1, 14, 0, 0, 18, 0, 0, 24, 0, 1, 29, 14, 40, 38]

"""
6, 1, 1, 0, 4, 2
6, 255, 1, 0, 4, 252

6, 4, 0, 255, 255, 2 
6, 4, 0, 0, 0, 2
6, 4, 1, 255, 255, 3
6, 4, 1, 0, 0, 3
6, 4, 2, 255, 255, 0
6, 4, 2, 0, 0, 0
6, 4, 4, 255, 255, 6
6, 4, 4, 0, 0, 6
6, 4, 7, 255, 255, 5 
6, 4, 7, 0, 56, 61
6, 4, 9, 255, 255, 11
6, 4, 9, 0, 0, 11
6, 4, 10, 255, 255, 8
6, 4, 10, 0, 0, 8
6, 4, 13, 255, 255, 15
6, 4, 13, 0, 1, 14
6, 4, 14, 255, 255, 12
6, 4, 14, 0, 0, 12
6, 4, 18, 255, 255, 16
6, 4, 18, 0, 0, 16
6, 4, 24, 255, 255, 26
6, 4, 24, 0, 1, 27
6, 4, 29, 255, 255, 31
6, 4, 29, 14, 40, 57
"""
kPANASONIC_FYTW_08810115_REGISTER_META = {
    "device": "Dehumidifier",
    "services": [
        "0x00: DevicePowerService(code 0x00, RW, min 0, max 3)",
        "0x01: DeviceOpModeService(code 0x01, RW, min 0, max 127)",
        "0x02: DeviceOpTimerService(code 0x02, RW, min 0, max 12)",
        "0x04: DeviceDehumidifierLevelService(code 0x04, RW, min 0, max 6)",
        "0x07: DeviceHumidityRService(code 0x07, R, min 0, max 0)",
        "0x09: DeviceFanDirectionLevelService(code 0x09, RW, min 0, max 15)",
        "0x0a: DeviceWaterFullAlarmRService(code 0x0a, R, min 0, max 0)",
        "0x0d: DeviceAirCleanModeService(code 0x0d, RW, min 0, max 3)",
        "0x0e: DeviceFanLevelService(code 0x0e, RW, min 0, max 15)",
        "0x12: DeviceDisplayErrRService(code 0x12, R, min 0, max 0)",
        "0x18: DeviceSaaCtrlAudioService(code 0x18, RW, min 0, max 3)",
        "0x1d: DeviceTotalWattService(code 0x1d, RW, min 0, max 0)"
    ],
    "brand": "Panasonic",
    "model": "FYTW-08810115",
    "cmds": [
        "0x00: power                 DevicePowerService",
        "0x01: op_mode               DeviceOpModeService",
        "0x02: op_timer              DeviceOpTimerService",
        "0x04: dehumidifier_level    DeviceDehumidifierLevelService",
        "0x07: humidity              DeviceHumidityRService",
        "0x09: fan_direction_level   DeviceFanDirectionLevelService",
        "0x0a: water_full_alarm      DeviceWaterFullAlarmRService",
        "0x0d: air_clean_mode        DeviceAirCleanModeService",
        "0x0e: fan_level             DeviceFanLevelService",
        "0x12: display_err           DeviceDisplayErrRService",
        "0x18: saa_ctrl_audio        DeviceSaaCtrlAudioService",
        "0x1d: total_watt            DeviceTotalWattService"
    ]
}
