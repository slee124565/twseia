"""**TWSEIA** is a Python library for TaiSEIA device via serial port (via USB, RS485 or RS232).

Examples:

    Read POWER state from TaiSEIA device::

        import twseia
        sa = twseia.SmartApplication()
        service_id = 0
        r = sa.read_state(service_id)

    Write POWER command to TaiSEIA device::

        import twseia
        sa = twseia.SmartApplication()
        service_id = 0
        POWER_ON = 1
        r = sa.write_state(service_id, POWER_ON)
        print(r.to_json())

"""

from .constants import *
from .packets import *
from .devices import *
from .services import *
from .smart_application import *
