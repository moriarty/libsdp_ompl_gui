#!/usr/bin/env python
"""
# Title: MPLViewer
# Description: View 2D ompl paths as MatPlotLib
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4.QtCore import pyqtSignal as Signal
from MplCanvas import MplCanvas
from numpy import arange, sin, pi, cos
import numpy as np

class MPLViewer(MplCanvas):
    """docstring for MPLViewer"""
    
    boundLowChanged = Signal(list)
    boundHighChanged = Signal(list)
    
    def __init__(self):
        super(MPLViewer, self).__init__()
        pass
    
    def setBounds(self, bounds):
        pass
