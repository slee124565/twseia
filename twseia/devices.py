import logging
from .services import SAServiceBase

logger = logging.getLogger(__name__)


class SAEngModeService(SAServiceBase):
    """工程模式"""
    pass


class SADevice:

    @classmethod
    def convert_dev_specific_service(cls, pdu: list, is_fixed_len_pdu: bool) -> SAServiceBase:
        raise NotImplementedError


__all__ = [
    'SAEngModeService',
    'SADevice',
]
