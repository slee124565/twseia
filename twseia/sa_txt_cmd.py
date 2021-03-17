from .services import SAServiceBase
from .packets import SARegisterPacket


def read_sa_cmd_helps(register: SARegisterPacket):
    assert isinstance(register, SARegisterPacket)
    _helps = []
    for _service in register.services:
        assert isinstance(_service, SAServiceBase)
        _helps.append(_service.to_cmd_help())
    return _helps


__all__ = [
    'read_sa_cmd_helps',
]
