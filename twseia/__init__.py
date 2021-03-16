
from .constants import *
from .packets import *
from .devices import *
from .services import *
from .smart_application import *
from .sa_txt_cmd import *
from .utils import *


def create_sa_register_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.REGISTRATION
    ).to_pdu()


def parsing_sa_register_response(pdu: list) -> SARegisterPacket:
    return SARegisterPacket.from_pdu(pdu=pdu)


def create_sa_class_id_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_CLASS_ID
    ).to_pdu()


def parsing_sa_class_id_response(pdu: list) -> int:
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_CLASS_ID:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return int.from_bytes(packet.data_bytes, 'big')


def create_sa_protocol_version_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_PROTOCOL_VERSION
    ).to_pdu()


def parsing_sa_protocol_version_response(pdu: list) -> tuple:
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_PROTOCOL_VERSION:
        raise ValueError(f'pdu service id invalid, {pdu}')
    if len(packet.data_bytes) != 2:
        raise ValueError(f'pdu data invalid, {pdu}')
    major = packet.data_bytes[0]
    minor = packet.data_bytes[1]
    return major, minor


def create_read_dev_type_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_TYPE_ID
    ).to_pdu()


def parsing_sa_dev_type_response(pdu: list) -> int:
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_TYPE_ID:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return int.from_bytes(packet.data_bytes, 'big')


def create_read_brand_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_BRAND
    ).to_pdu()


def parsing_sa_brand_response(pdu: list) -> str:
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_BRAND:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return bytearray(packet.data_bytes).decode('utf-8')


def create_read_model_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_MODEL
    ).to_pdu()


def parsing_sa_model_response(pdu: list) -> str:
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_MODEL:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return bytearray(packet.data_bytes).decode('utf-8')


def create_read_supported_services_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_SUPPORTED_SERVICES
    ).to_pdu()


def parsing_dehumidifier_services_response(pdu: list) -> list:
    """
    40 len, 0 type_id, 7 service_id,
    128, 0, 3,
    129, 0, 127,
    130, 0, 12,
    132, 0, 6,
    7, 0, 0,
    137, 0, 15,
    10, 0, 0,
    141, 0, 3,
    142, 0, 15,
    18, 0, 0,
    152, 0, 3,
    157, 0, 0,
    206 checksum
    """


def create_current_states_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_CURRENT_SERVICES_STATES
    ).to_pdu()


def parsing_sa_all_states_response(pdu: list):
    """
    40 len, 0 type_id, 8 service_id,
    0, 0, 0,
    1, 0, 0,
    2, 0, 0,
    4, 0, 0,
    7, 0, 55,
    9, 0, 0,
    10, 0, 0,
    13, 0, 1,
    14, 0, 0,
    18, 0, 0,
    24, 0, 1,
    29, 14, 40,
    38 checksum
    """
