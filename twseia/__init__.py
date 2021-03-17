import logging
from .constants import *
from .packets import *
from .devices import *
from .services import *
from .smart_application import *
from .sa_txt_cmd import *
from .utils import *
from .dehumidifier import *
from .air_conditioner import *


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
    return bytearray(packet.data_bytes[:-1]).decode('utf-8')


def create_read_model_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_MODEL
    ).to_pdu()


def parsing_sa_model_response(pdu: list) -> str:
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if packet.service_id != SARegisterServiceIDEnum.READ_MODEL:
        raise ValueError(f'pdu service id invalid, {pdu}')
    return bytearray(packet.data_bytes[:-1]).decode('utf-8')


def create_read_supported_services_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_SUPPORTED_SERVICES
    ).to_pdu()


def parsing_dehumidifier_services_response(pdu: list, is_fixed_len_pdu: bool = True) -> list:
    """"""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if not is_fixed_len_pdu:
        raise NotImplementedError
    n = 0
    _services = []
    logging.debug(f'data_bytes {packet.data_bytes}')
    while n < len(packet.data_bytes):
        service = Dehumidifier.convert_dev_specific_service(
            pdu=packet.data_bytes[n:n+3], is_fixed_len_pdu=is_fixed_len_pdu)
        logging.debug(f'cmd_help {service.to_cmd_help()}')
        _services.append(service.to_cmd_help().to_json())
        n += 3
    return _services


def create_read_all_states_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_CURRENT_SERVICES_STATES
    ).to_pdu()


def parsing_dehumidifier_all_states_response(pdu: list, is_fixed_len_pdu: bool = True):
    """"""
    packet = SAInfoResponsePacket.from_pdu(pdu=pdu)
    if not is_fixed_len_pdu:
        raise NotImplementedError
    n = 0
    response = []
    while n < len(packet.data_bytes):
        service = Dehumidifier.convert_dev_specific_service(
            pdu=packet.data_bytes[n:n+3], is_fixed_len_pdu=is_fixed_len_pdu)
        # service = service.to_cmd_help()
        response.append({'name': service.name, 'value': service.read_value()})
        n += 3
    return response


def create_read_state_cmd(type_id: int, service_id: int) -> list:
    """"""
    return SAStateReadRequestPacket.create(
        type_id=type_id,
        service_id=service_id
    ).to_pdu()


def parsing_read_state_response(pdu: list, is_fixed_len_pdu: bool = True) -> SAServiceBase:
    """"""
    if not is_fixed_len_pdu:
        raise NotImplementedError

    _service = SAServiceBase.from_fixed_len_pdu(pdu=pdu)
    return _service.read_value()
