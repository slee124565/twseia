
from .constants import *
from .packets import *
from .devices import *
from .services import *
from .smart_application import *
from .sa_txt_cmd import *
from .utils import *


def create_read_register_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.REGISTRATION
    ).to_pdu()


def create_read_class_id_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_CLASS_ID
    ).to_pdu()


def create_read_protocol_version_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_PROTOCOL_VERSION
    ).to_pdu()


def create_read_dev_type_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_TYPE_ID
    ).to_pdu()


def create_read_brand_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_BRAND
    ).to_pdu()


def create_read_model_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_MODEL
    ).to_pdu()


def create_read_supported_services_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_SUPPORTED_SERVICES
    ).to_pdu()


def create_current_states_cmd():
    return SAInfoRequestPacket.create(
        sa_info_type=SARegisterServiceIDEnum.READ_CURRENT_SERVICES_STATES
    ).to_pdu()


def parsing_read_register_response(pdu: list) -> SAInfoRegisterPacket:
    return SAInfoRegisterPacket.from_pdu(pdu=pdu)
