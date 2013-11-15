#!/usr/bin/env python
"""
# Title: MyStaticMplCanvas
# Description: Simple Static MatPlotLib Canvas for testing MPL in Qt
# Author: @moriarty, @amdshameer
# Licence: 
"""


from PyQt4.QtCore import pyqtSignal as Signal
from MplCanvas import MplCanvas
from numpy import arange, sin, pi, cos
import numpy as np


## MyStaticMplCanvas is a place holder for now
## Will redo to plot path once input fields completed
class MyStaticMplCanvas(MplCanvas):
    """Simple canvas with a sine plot."""
    boundLowChanged = Signal(list)
    boundHighChanged = Signal(list)

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)

    def refresh(self):
        self.boundsChanged()
        self.draw()

    def plot(self):
        t = arange(0.0, 3.0, 0.01)
        s = cos(2*pi*t)
        self.axes.plot(t,s)
        self.refresh()

    def boundsChanged(self):
        xmin, xmax, ymin, ymax = self.axes.axis()
        self.boundLowChanged.emit([xmin, ymin])
        self.boundHighChanged.emit([xmax, ymax])

    def setBounds(self,upper=None,lower=None):
        xmin, xmax, ymin, ymax = None, None, None, None
        if upper:
            xmax = upper[0]
            ymax = upper[1]
        if lower:
            xmin = lower[0]
            ymin = lower[1]
        self.axes.axis([xmin, xmax, ymin, ymax])
        self.refresh()

    def setLowerBounds(self,bounds):
        self.setBounds(lower=bounds)

    def setUpperBounds(self,bounds):
        self.setBounds(upper=bounds)

    def resetBounds(self):
        self.setBounds(upper=[10,10], lower=[-10,-10])
        self.refresh()