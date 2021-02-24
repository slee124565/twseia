from .constants import *
from .packets import CommonPacket

def _create_payload(type_id: int, service_id: int, cmd_id: int, cmd_value: int):
    if type_id is None:
        raise Exception('No SA Type ID assigned. Execute [register] first.')

    _payload = [6,
                type_id,
                (cmd_id << 7) | service_id,
                ] + list(cmd_value.to_bytes(2, 'big')) + [0]
    for x in _payload[:-1]:
        _payload[-1] ^= x
    return _payload


def _parse_payload(payload: list):
    raise NotImplementedError


class SmartApplication:

    def __init__(self, port='/dev/ttyUSB0'):
        """"""
        self.port = port
        self._type_id = None

    def _request(self, payload):
        raise NotImplementedError

    def register(self):
        """Send a Register request for SA."""
        packet = CommonPacket.create_packet(
            sa_dev_type=SADeviceType.REGISTER,
            cmd_type=SACmdType.READ,
            sa_service=SAServiceID.REGISTER,
        )
        resp = self._request(payload=packet.to_pdu())
        return resp

    def read_service(self, service_id: int):
        """Send a Read request for SA."""
        _payload = _create_payload(
            type_id=self._type_id,
            service_id=service_id,
            cmd_id=SACmdType.READ.value,
            cmd_value=0xffff
        )
        resp = self._request(payload=_payload)
        return resp

    def write_service(self, service_id: int, value: int):
        """Send a Write request for SA."""
        _payload = _create_payload(
            type_id=self._type_id,
            service_id=service_id,
            cmd_id=SACmdType.WRITE.value,
            cmd_value=value
        )
        resp = self._request(payload=_payload)
        return resp


__all__ = ['SmartApplication', '_create_payload']
