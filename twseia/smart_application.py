"""SmartApplication: A Python driver for TaiSEIA protocol device control via serial port (via USB, RS485 or RS232)."""

from tests.sample_pdus import kHITACHI_AC_RAD_50NK_REGISTER_PDU
from .constants import SARegisterServiceID
from .constants import SADeviceType
from .packets import SAInfoRequestPacket
from .packets import SAInfoRegisterPacket
from .packets import SAStateReadRequestPacket
from .packets import SAStateReadResponsePacket
from .packets import SAStateWriteRequestPacket
from .packets import SAStateWriteResponsePacket


class SmartApplication:
    """SmartApplication(SA) class for talking to TaiSEIA Smart Application device.

    Uses TaiSEIA protocol via RS232

    Attributes:
        port (str): The serial port name, for example ``/dev/ttyUSB0`` (Linux),
        ``/dev/tty.usbserial`` (OS X) or ``COM4`` (Windows).
    """
    _device = None

    def __init__(self, port='/dev/ttyUSB0'):
        """"""
        self.port = port
        # self.register()

    @property
    def services(self) -> list:
        """SA Service command `SAService` supported list."""
        if isinstance(self._device, SAInfoRegisterPacket):
            return self._device.services
        else:
            return []

    def request(self, payload: list) -> list:
        """Send a TaiSEIA protocol request bytes packet for SA.

        todo: Send bytes via real RS232.

        """
        req = SAInfoRequestPacket.from_pdu(payload)
        if req.type_id == 0x00 and req.service_id == SARegisterServiceID.READ_ALL:
            # return SAInfoResponsePacket.from_pdu(pdu=kHITACHI_AC_RAD_50NK_REGISTER_PDU)
            return kHITACHI_AC_RAD_50NK_REGISTER_PDU
        else:
            if req.type_id == SADeviceType.AIR_CONDITIONER:
                if payload == [0x06, 0x01, 0x00, 0xff, 0xff, 0x07]:
                    return [0x06, 0x01, 0x00, 0x00, 0x00, 0x07]
                elif payload == [0x06, 0x01, 0x01, 0xff, 0xff, 0x06]:
                    return [0x06, 0x01, 0x01, 0x00, 0x04, 0x02]
                elif payload == [0x06, 0x01, 0x02, 0xff, 0xff, 0x05]:
                    return [0x06, 0x01, 0x02, 0x00, 0x01, 0x04]
                elif payload == [0x06, 0x01, 0x03, 0xff, 0xff, 0x04]:
                    return [0x06, 0x01, 0x03, 0x00, 0x19, 0x1d]
                elif payload == [0x06, 0x01, 0x04, 0xff, 0xff, 0x03]:
                    return [0x06, 0x01, 0x04, 0x00, 0x19, 0x1a]
                elif payload == [0x06, 0x01, 0x06, 0xff, 0xff, 0x01]:
                    return [0x06, 0x01, 0x06, 0x00, 0x00, 0x01]
                elif payload == [0x06, 0x01, 0x0b, 0xff, 0xff, 0x0c]:
                    return [0x06, 0x01, 0x0b, 0x00, 0x00, 0x0c]
                elif payload == [0x06, 0x01, 0x0c, 0xff, 0xff, 0x0b]:
                    return [0x06, 0x01, 0x0c, 0x00, 0x00, 0x0b]
                elif payload == [0x06, 0x01, 0x17, 0xff, 0xff, 0x10]:
                    return [0x06, 0x01, 0x17, 0x00, 0x00, 0x10]
                elif payload == [0x06, 0x01, 0x1a, 0xff, 0xff, 0x1d]:
                    return [0x06, 0x01, 0x1a, 0x00, 0x00, 0x1d]
                elif payload == [0x06, 0x01, 0x1b, 0xff, 0xff, 0x1c]:
                    return [0x06, 0x01, 0x1b, 0x00, 0x00, 0x1c]
                elif payload == [0x06, 0x01, 0x1d, 0xff, 0xff, 0x1a]:
                    return [0x06, 0x01, 0x1d, 0x00, 0x00, 0x1a]
                elif payload == [0x06, 0x01, 0x1e, 0xff, 0xff, 0x19]:
                    return [0x06, 0x01, 0x1e, 0x00, 0x00, 0x19]
                elif payload == [0x06, 0x01, 0x21, 0xff, 0xff, 0x26]:
                    return [0x06, 0x01, 0x21, 0x00, 0x11, 0x37]
                elif payload == [0x06, 0x01, 0x28, 0xff, 0xff, 0x2f]:
                    return [0x06, 0x01, 0x28, 0x0f, 0x80, 0xa0]
                elif payload == [0x06, 0x01, 0x29, 0xff, 0xff, 0x2e]:
                    return [0x06, 0x01, 0x29, 0x00, 0x00, 0x2e]
                elif payload == [0x06, 0x01, 0x2f, 0xff, 0xff, 0x28]:
                    return [0x06, 0x01, 0x2f, 0x0b, 0xd6, 0xf5]
                elif payload == [0x06, 0x01, 0x30, 0xff, 0xff, 0x37]:
                    return [0x06, 0x01, 0x30, 0x03, 0x20, 0x14]
                elif payload == [0x06, 0x01, 0x00, 0xff, 0xff, 0x07]:
                    return [0x06, 0x01, 0x00, 0x00, 0x00, 0x07]
                else:
                    raise NotImplementedError
            else:
                raise NotImplementedError

    def register(self) -> SAInfoRegisterPacket:
        """Send a Register request packet for SA."""
        payload = SAInfoRequestPacket.create(
            sa_info_type=SARegisterServiceID.READ_ALL
        ).to_pdu()
        response = self.request(payload=payload)
        device = SAInfoRegisterPacket.from_pdu(pdu=response)
        self._device = device
        return device

    def read_state(self, service_id) -> SAStateReadResponsePacket:
        """Send a State Read request packet for SA."""
        payload = SAStateReadRequestPacket.create(
            type_id=self._device.type_id,
            service_id=service_id
        ).to_pdu()
        response = self.request(payload=payload)
        print(f'response: {response}')
        response = SAStateReadResponsePacket.from_pdu(pdu=response)
        assert isinstance(response, SAStateReadResponsePacket)
        return response

    # def read_sensor(self, service_id) -> SASensorReadMultiResponsePacket:
    #     """Send a Sensor Read request for SA."""
    #     raise NotImplementedError

    def write_state(self, service_id, value) -> SAStateWriteResponsePacket:
        """Send a State Write request packet for SA."""
        payload = SAStateWriteRequestPacket.create(
            type_id=self._device.type_id,
            service_id=service_id,
            value=value
        ).to_pdu()
        response = self.request(payload=payload)
        response = SAStateWriteResponsePacket.from_pdu(pdu=response)
        assert isinstance(response, SAStateWriteResponsePacket)
        return response


__all__ = ['SmartApplication']
