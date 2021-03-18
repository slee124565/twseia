import enum
import logging
from .services import SAServiceBase

logger = logging.getLogger(__name__)


class SAEngModeService(SAServiceBase):
    """工程模式"""
    pass


class SADevice:
    @classmethod
    def read_spec_cmd_helps(cls) -> list:
        raise NotImplementedError

    @classmethod
    def read_service_id_list(cls) -> list:
        raise NotImplementedError

    @classmethod
    def read_type_id(cls) -> int:
        raise NotImplementedError

    @classmethod
    def read_cmd_list(cls) -> list:
        raise NotImplementedError

    @classmethod
    def convert_cmd_txt_to_service_id(cls, cmd_txt: str) -> int:
        raise NotImplementedError

    @classmethod
    def convert_dev_specific_service(cls, pdu: list, is_fixed_len_pdu: bool) -> SAServiceBase:
        raise NotImplementedError


__all__ = [
    'SAEngModeService',
    'SADevice',
]
