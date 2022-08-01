from pylab import *
from Instruments import Bridge12, prologix_connection, gigatronics
from Instruments.bridge12 import convert_to_power, convert_to_mv
from serial import Serial
import time
from itertools import cycle

# {{{ Qt5 stuff
import sys, os, random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
# }}}

meter_readings = []

if run_bridge12:
    with Bridge12() as b:
        b.set_wg(True)
        b.set_rf(True)
        b.set_amp(True)
        time.sleep(5)
        _,dip_f = b.lock_on_dip(ini_range=(9.819e9,9.825e9))
