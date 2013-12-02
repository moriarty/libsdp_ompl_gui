#!/usr/bin/env python
"""
# Title: MPLViewer
# Description: View 2D ompl paths as MatPlotLib
# Author: @moriarty, @amdshameer
# Licence: 
"""

from ompl_gui.plot_view.MplCanvas import MplCanvas
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

class MPLViewer(MplCanvas):
    """docstring for MPLViewer"""

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
        self.axes.axis([-10, 10, -10, 10])

    def refresh(self):
        self.draw()

    def plot(self, x, y, label):
        self.axes.plot(x, y, label=label)
        self.axes.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
            loc=3, ncol=4, mode="expand", borderaxespad=0.)
        self.refresh()

    def setBounds(self, upper=None, lower=None):
        xmin, xmax, ymin, ymax = -10.0, 10.0, -10.0, 10.0
        if upper:
            xmax = upper[0]
            ymax = upper[1]
        if lower:
            xmin = lower[0]
            ymin = lower[1]
        self.axes.axis([xmin, xmax, ymin, ymax])
        self.refresh()

    def setLowerBounds(self, bounds):
        self.setBounds(lower=bounds)

    def setUpperBounds(self, bounds):
        self.setBounds(upper=bounds)

    def resetBounds(self):
        self.setBounds(upper=[10, 10], lower=[-10, -10])
        self.refresh()
