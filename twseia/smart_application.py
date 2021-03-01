from .constants import SARegisterServiceID
from .packets import SAInfoRequestPacket
from .packets import SAInfoRegisterPacket
from .packets import SAStateReadRequestPacket
from .packets import SAStateReadResponsePacket
from .packets import SAStateWriteRequestPacket
from .packets import SAStateWriteResponsePacket


class SmartApplication:
    class_id = None
    type_id = None
    services = None
    version = None
    brand = None
    model = None

    def __init__(self, port='/dev/ttyUSB0'):
        """"""
        self.port = port

    def request(self, payload):
        """Send a Packet request for SA."""
        raise NotImplementedError

    def register(self) -> SAInfoRegisterPacket:
        """Send a Register request for SA."""
        payload = SAInfoRequestPacket.create(
            sa_info_type=SARegisterServiceID.READ_ALL
        ).to_pdu()
        resp = self.request(payload=payload)
        assert isinstance(resp, SAInfoRegisterPacket)
        self.type_id = resp.type_id
        self.class_id = resp.class_id
        self.version = (resp.major_ver, resp.minor_ver)
        self.brand = resp.brand
        self.model = resp.model
        self.services = resp.services
        return resp

    def read_state(self, service_id) -> SAStateReadResponsePacket:
        """Send a State Read request for SA."""
        payload = SAStateReadRequestPacket.create(
            type_id=self.type_id,
            service_id=service_id
        ).to_pdu()
        resp = self.request(payload=payload)
        assert isinstance(resp, SAStateReadResponsePacket)
        return resp

    # def read_sensor(self, service_id) -> SASensorReadMultiResponsePacket:
    #     """Send a Sensor Read request for SA."""
    #     raise NotImplementedError

    def write_state(self, service_id, value) -> SAStateWriteResponsePacket:
        """Send a State Write request for SA."""
        payload = SAStateWriteRequestPacket.create(
            type_id=self.type_id,
            service_id=service_id,
            value=value
        ).to_pdu()
        resp = self.request(payload=payload)
        assert isinstance(resp, SAStateWriteResponsePacket)
        return resp


__all__ = ['SmartApplication']
