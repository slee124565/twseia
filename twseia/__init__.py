import logging
from .constants import *
from .packets import *
from .devices import *
from .services import *
from .sa_txt_cmd import *
from .utils import *
from .dehumidifier import *
from .air_conditioner import *

logger = logging.getLogger(__name__)
SUPPORT_SA_TYPE_ID_LIST = [
    SATypeIDEnum.DEHUMIDIFIER.value,
    SATypeIDEnum.AIR_CONDITIONER.value
]


def read_sa_type_id_dict() -> dict:
    """Read TaiSEIA Smart Application (SA) device type name and ID from twseia library."""
    dev_type_id_dict = {}
    for n in list(SATypeIDEnum):
        dev_type_id_dict[n.name] = n.value
    return dev_type_id_dict


def create_sa_register_cmd() -> list:
    """Create TaiSEIA register request protocol data."""
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.REGISTRATION
    ).to_pdu()


def parsing_sa_register_response(pdu: list) -> SARegisterPacket:
    """Parsing TaiSEIA register response protocol data."""
    return SARegisterPacket.from_pdu(pdu=pdu)


def read_sa_cmd_helps_from_register_response(pdu: list) -> list:
    """Read TaiSEIA SA device supported commands from register response protocol data."""
    register = SARegisterPacket.from_pdu(pdu)
    report = []
    for service in register.services:
        _help = service.to_cmd_help()
        assert isinstance(_help, SACmdHelp)
        report.append(_help.to_json())
    return report


def create_sa_class_id_cmd() -> list:
    """Create TaiSEIA class ID request protocol data."""
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_CLASS_ID
    ).to_pdu()


def parsing_sa_class_id_response(pdu: list) -> int:
    """Parsing TaiSEIA class ID response protocol data."""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_CLASS_ID:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return int.from_bytes(packet.data_bytes, 'big')


def create_sa_protocol_version_cmd() -> list:
    """Create TaiSEIA device version request protocol data."""
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_PROTOCOL_VERSION
    ).to_pdu()


def parsing_sa_protocol_version_response(pdu: list) -> tuple:
    """Parsing TaiSEIA device protocol version response protocol data."""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_PROTOCOL_VERSION:
        raise ValueError(f'pdu service id invalid, {pdu}')
    if len(packet.data_bytes) != 2:
        raise ValueError(f'pdu data invalid, {pdu}')
    major = packet.data_bytes[0]
    minor = packet.data_bytes[1]
    return major, minor


def create_read_dev_type_cmd() -> list:
    """Create TaiSEIA device type request protocol data."""
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_TYPE_ID
    ).to_pdu()


def parsing_sa_dev_type_response(pdu: list) -> int:
    """Parsing TaiSEIA device type ID response protocol data."""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_TYPE_ID:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return int.from_bytes(packet.data_bytes, 'big')


def create_read_brand_cmd() -> list:
    """Create TaiSEIA device brand request protocol data."""
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_BRAND
    ).to_pdu()


def parsing_sa_brand_response(pdu: list) -> str:
    """Parsing TaiSEIA device brand response protocol data."""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_BRAND:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return bytearray(packet.data_bytes[:-1]).decode('utf-8')


def create_read_model_cmd() -> list:
    """Create TaiSEIA device model request protocol data."""
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_MODEL
    ).to_pdu()


def parsing_sa_model_response(pdu: list) -> str:
    """Parsing TaiSEIA device model response protocol data."""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_MODEL:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return bytearray(packet.data_bytes[:-1]).decode('utf-8')


def create_read_supported_services_cmd() -> list:
    """Create TaiSEIA device services request protocol data."""
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_SUPPORTED_SERVICES
    ).to_pdu()


def parsing_sa_services_response(type_id: int, pdu: list, is_fixed_len_pdu: bool = True) -> list:
    """Parsing TaiSEIA Dehumidifier device services response protocol data."""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if not is_fixed_len_pdu:
        raise NotImplementedError
    if type_id == SATypeIDEnum.DEHUMIDIFIER:
        dev_cls = Dehumidifier
    elif type_id == SATypeIDEnum.AIR_CONDITIONER:
        dev_cls = AirConditioner
    else:
        raise ValueError(f'type_id {type_id} not supported!')
    assert issubclass(dev_cls, SADevice)

    n = 0
    _services = []
    logging.debug(f'data_bytes {packet.data_bytes}')
    while n < len(packet.data_bytes):
        service = dev_cls.convert_dev_specific_service(
            pdu=packet.data_bytes[n:n + 3], is_fixed_len_pdu=is_fixed_len_pdu)
        logging.debug(f'cmd_help {service.to_cmd_help()}')
        _services.append(service.to_cmd_help().to_json())
        n += 3
    return _services


def create_read_all_states_cmd() -> list:
    """Create TaiSEIA device all states request protocol data."""
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_CURRENT_SERVICES_STATES
    ).to_pdu()


def parsing_sa_all_states_response(type_id: int, pdu: list, is_fixed_len_pdu: bool = True) -> list:
    """Parsing TaiSEIA Dehumidifier all service states response protocol data."""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if not is_fixed_len_pdu:
        raise NotImplementedError
    if type_id == SATypeIDEnum.DEHUMIDIFIER:
        dev_cls = Dehumidifier
    elif type_id == SATypeIDEnum.AIR_CONDITIONER:
        dev_cls = AirConditioner
    else:
        raise ValueError(f'type_id {type_id} not supported!')
    assert issubclass(dev_cls, SADevice)

    n = 0
    response = []
    while n < len(packet.data_bytes):
        service = dev_cls.convert_dev_specific_service(
            pdu=packet.data_bytes[n:n + 3], is_fixed_len_pdu=is_fixed_len_pdu)
        # service = service.to_cmd_help()
        report = {'description': service.description, 'value': service.read_value()}
        if service.unit is not None:
            report['unit'] = service.unit
        response.append(report)
        n += 3
    return response


def create_read_state_cmd(type_id: int, service_id: int) -> list:
    """Create TaiSEIA device service state request protocol data."""
    return SAStateReadRequestPacket.create(
        type_id=type_id,
        service_id=service_id
    ).to_pdu()


def create_read_state_cmd_from_txt(type_id: int, cmd_txt: str) -> list:
    """Create TaiSEIA device service state request protocol data from text cmd."""
    if type_id == SATypeIDEnum.DEHUMIDIFIER:
        service_id = Dehumidifier.convert_cmd_txt_to_service_id(cmd_txt=cmd_txt)
    elif type_id == SATypeIDEnum.AIR_CONDITIONER:
        service_id = AirConditioner.convert_cmd_txt_to_service_id(cmd_txt=cmd_txt)
    else:
        raise NotImplementedError

    return SAStateReadRequestPacket.create(
        type_id=type_id, service_id=service_id
    ).to_pdu()


def parsing_read_state_response(type_id: int, pdu: list, is_fixed_len_pdu: bool = True) -> dict:
    """Parsing TaiSEIA device service state response protocol data."""
    if not is_fixed_len_pdu:
        raise NotImplementedError

    if type_id == SATypeIDEnum.DEHUMIDIFIER:
        dev_cls = Dehumidifier
    elif type_id == SATypeIDEnum.AIR_CONDITIONER:
        dev_cls = AirConditioner
    else:
        raise NotImplementedError
    assert issubclass(dev_cls, SADevice)

    packet = SAStateReadResponsePacket.from_pdu(pdu=pdu)
    if packet.type_id != type_id:
        raise ValueError(f'pdu type_id invalid, {pdu}')
    _service = dev_cls.convert_dev_specific_service(pdu=pdu[2:-1], is_fixed_len_pdu=True)
    return _service.to_state_report()


def create_write_state_cmd_from_txt(type_id: int, cmd_txt: str, cmd_value: int) -> list:
    """Create TaiSEIA device service state write request protocol data from text cmd."""
    if type_id == SATypeIDEnum.DEHUMIDIFIER:
        service_id = Dehumidifier.convert_cmd_txt_to_service_id(cmd_txt=cmd_txt)
    elif type_id == SATypeIDEnum.AIR_CONDITIONER:
        service_id = AirConditioner.convert_cmd_txt_to_service_id(cmd_txt=cmd_txt)
    else:
        raise NotImplementedError

    return SAStateWriteRequestPacket.create(
        type_id=type_id, service_id=service_id, value=cmd_value
    ).to_pdu()

# def create_write_cmd_from_txt(dev_txt: str, cmd_txt: str, value_txt: str) -> list:
#     """"""
#     if not f'{value_txt}'.isnumeric():
#         raise ValueError(f'value_txt not numeric, {value_txt}')
#     dev_type_id_dict = {}
#     for n in list(SATypeIDEnum):
#         dev_type_id_dict[n.name] = n.value
#     logger.debug(f'{dev_type_id_dict.keys()}')
#     _name = dev_txt.upper()
#     if _name not in dev_type_id_dict.keys():
#         raise ValueError(f'dev_txt invalid, {dev_txt}')
#     type_id = dev_type_id_dict[_name]
#     return create_write_state_cmd_from_txt(
#         type_id=type_id, cmd_txt=cmd_txt, cmd_value=int(value_txt))
