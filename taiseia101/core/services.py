
from base_dev_service import *

import logging
logger = logging.getLogger(__name__)


class PowerRWService(DeviceEnum16Service):

    def __init__(self, serv_pdu):
        super(PowerRWService, self).__init__(serv_pdu)


class OpModeRWService(DeviceEnum16Service):

    def __init__(self, serv_pdu):
        super(OpModeRWService, self).__init__(serv_pdu)


