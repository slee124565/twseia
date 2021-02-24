"""
import twseia
sa = twseia.SmartApplication('/dev/ttyUSB1')
sa.read_capability()
sa.read
sa.write
"""

from .constants import *
from .smart_application import *
