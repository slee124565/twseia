from .devices import ACServiceIDEnum
from .services import SAServiceBase
from .packets import SAInfoRegisterPacket


def read_sa_cmd_helps(register: SAInfoRegisterPacket):
    assert isinstance(register, SAInfoRegisterPacket)
    _helps = []
    for _service in register.services:
        assert isinstance(_service, SAServiceBase)
        _helps.append(_service.to_cmd_help())
    return _helps


__all__ = [
    'read_sa_cmd_helps',
]
