#!/usr/bin/env python
"""
# Title: MplCanvas Superclass
# Description: MplCanvas is a FigureCanvas to display matplotlib plots in Qt
# Author: @moriarty, @amdshameer
# Licence: 
"""

# Import statements
from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

## MplCanvas and MyStaticMplCanvas from embedding_in_qt4 tutorial on matplotlib site.
class MplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        #fig, axes = plt.subplots(1)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

    def clear(self):
        self.axes.clear()
        self.draw()
