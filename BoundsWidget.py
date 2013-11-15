#!/usr/bin/env python
"""
# Title: BoundsWidget
# Description: BoundsWidget is to set the bound parameters
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement

from PyQt4 import QtCore, QtGui
from BoundsBox import BoundsBox

# BoundsWidget class 

class BoundsWidget(QtGui.QWidget):
    def __init__(self):
        super(BoundsWidget, self).__init__()
        self.bounds_high = BoundsBox('Upper bounds')
        self.bounds_low = BoundsBox('Lower bounds')
        self.resetButton = QtGui.QPushButton('Reset')
        layout = QtGui.QGridLayout()
        layout.addWidget(self.bounds_high, 0,0)
        layout.addWidget(self.bounds_low, 1,0)
        layout.addWidget(self.resetButton, 2,0, QtCore.Qt.AlignRight)
        self.setLayout(layout)