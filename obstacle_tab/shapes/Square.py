#!/usr/bin/env python
"""
# Title: Square
# Description: A square obstacle
# Author: @moriarty, @amdshameer
# Licence:
"""
# import statement
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal as Signal
from matplotlib.path import Path
import numpy as np

def xy_from_htheta(h, theta):
    rtheta = theta*np.pi/180
    x = np.cos(rtheta)/h
    y = np.sin(rtheta)/h
    return (x, y)

# Square class
class Square(QtGui.QGroupBox):
    """
    Simple Square obstacle
    """
    sizeChanged = Signal(list)

    codes = [Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
        ]

    def __init__(self, title):
        super(Square, self).__init__(title)
        sizeLabel = QtGui.QLabel('Square Size')

        self.vertices = None
        
        self.size = QtGui.QDoubleSpinBox()
        self.size.setRange(1, 10)
        self.size.setSingleStep(0.5)

        layout = QtGui.QGridLayout()
        layout.addWidget(sizeLabel, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.size, 1, 1)
        self.setLayout(layout)

        ## Connect a change in size to sizeChange()
        self.size.valueChanged.connect(self.sizeChange)

    def setVertices(self, xcentre=0.0, ycentre=0.0, theta=0.0, size=1):
        angles = np.array([45, 135, 225, 315]) + theta
        distance = np.sqrt(2*size**2)/2
        xy_centre = np.array([[xcentre], [ycentre]])
        x, y = xy_from_htheta(distance, angles) + xy_centre
        verts = zip(x, y)
        verts.append(verts[0])
        self.vertices = verts

    def getVertices(self):
        return self.vertices

    def getPathCodes(self):
        return self.codes

    def setSize(self, value):
        """setBounds
        allows connections to set bounds
        """
        self.size.setValue(value[0])

    def getSize(self):
        """ returns bounds: [ size ] """
        return [self.size.value()]

    def sizeChange(self):
        """Emits ValueChanged Signal [ size]"""
        self.valueChanged.emit(self.getSize())
