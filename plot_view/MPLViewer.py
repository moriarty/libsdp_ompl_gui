#!/usr/bin/env python
"""
# Title: MPLViewer
# Description: View 2D ompl paths as MatPlotLib
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4.QtCore import pyqtSignal as Signal
from ompl_gui.plot_view.MplCanvas import MplCanvas
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

class MPLViewer(MplCanvas):
    """docstring for MPLViewer"""
    boundLowChanged = Signal(list)
    boundHighChanged = Signal(list)

    verts = [
        (5., 5.), # left, bottom
        (5., 8.), # left, top
        (8., 8.), # right, top
        (8., 5.), # right, bottom
        (5., 5.), # ignored
        ]

    codes = [Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
        ]

    def compute_initial_figure(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)
        self.axes.plot(t, s)
        path = Path(self.verts, self.codes)
        patch = patches.PathPatch(path, facecolor='orange', lw=2)
        self.axes.add_patch(patch)
        self.axes.axis([-10,10,-10,10])

    def refresh(self):
        self.boundsChanged()
        self.draw()

    def plot(self,x,y,label):
        self.axes.plot(x,y, label=label)
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

