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

# Square class
class Square(QtGui.QGroupBox):
    """
    Simple Square obstacle
    """
    valueChanged = Signal(list)

    def __init__(self, title):
        super(Square, self).__init__(title)
        sizeLabel = QtGui.QLabel('Size')
        
        self.size = QtGui.QDoubleSpinBox()
        self.size.setRange(1, 10)
        self.size.setSingleStep(0.5)

        layout = QtGui.QGridLayout()
        layout.addWidget(xlabel, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(ylabel, 2, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.posx, 1, 1)
        layout.addWidget(self.posy, 2, 1)
        self.setLayout(layout)

        ## Connect a change in posx or posy to boundsChange()
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

    def boundsChange(self, value):
        """Emits ValueChanged Signal [ x, y]"""
        self.valueChanged.emit([ self.posx.value(), self.posy.value() ])
