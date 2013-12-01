#!/usr/bin/env python
"""
# Title:BoundsBox
# Description: BoundsBox for selecting the bound limits
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal as Signal

# BoundsBox class
class BoundsBox(QtGui.QGroupBox):
    """
    Simple 2D bounds. 

    Same as Bounds Box in ompl_app but only 2D
    """
    valueChanged = Signal(list)

    def __init__(self, title):
        super(BoundsBox, self).__init__(title)
        xlabel = QtGui.QLabel('X')
        ylabel = QtGui.QLabel('Y')

        self.posx = QtGui.QDoubleSpinBox()
        self.posx.setRange(-100, 100)
        self.posx.setSingleStep(0.5)
        self.posy = QtGui.QDoubleSpinBox()
        self.posy.setRange(-100, 100)
        self.posy.setSingleStep(0.5)

        layout = QtGui.QGridLayout()
        layout.addWidget(xlabel, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(ylabel, 2, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.posx, 1, 1, QtCore.Qt.AlignLeft)
        layout.addWidget(self.posy, 2, 1, QtCore.Qt.AlignLeft)
        self.setLayout(layout)

        self.posx.valueChanged.connect(self.boundsChange)
        self.posy.valueChanged.connect(self.boundsChange)


    def setBounds(self, value):
        """setBounds
        allows connections to set bounds 
        """
        self.posx.setValue(value[0])
        self.posy.setValue(value[1])

    def getBounds(self):
        """ returns bounds: [x , y] """
        return [self.posx.value(), self.posy.value()]

    def boundsChange(self):
        """Emits ValueChanged Signal [ x, y]"""
        self.valueChanged.emit([ self.posx.value(), self.posy.value() ])

