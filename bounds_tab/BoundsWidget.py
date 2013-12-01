#!/usr/bin/env python
"""
# Title: BoundsWidget
# Description: BoundsWidget is to set the bound parameters
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement

from PyQt4 import QtCore, QtGui
from ompl_gui.bounds_tab.BoundsBox import BoundsBox

UPPER_BOUNDS = [10.0,10.0]
LOWER_BOUNDS = [-10.0,-10.0]

# BoundsWidget class 

class BoundsWidget(QtGui.QWidget):
    def __init__(self):
        super(BoundsWidget, self).__init__()
        self.bounds_high = BoundsBox('Upper bounds')
        self.bounds_low = BoundsBox('Lower bounds')
        self.bounds_high.setBounds(UPPER_BOUNDS)
        self.bounds_low.setBounds(LOWER_BOUNDS)
        self.resetButton = QtGui.QPushButton('Reset')
        self.applyButton = QtGui.QPushButton('Apply')
        layout = QtGui.QGridLayout()
        layout.addWidget(self.bounds_high, 0,0, 1, 2 )
        layout.addWidget(self.bounds_low, 1,0, 1, 2)
        layout.addWidget(self.resetButton, 2,0, QtCore.Qt.AlignRight)
        layout.addWidget(self.applyButton, 2,1, QtCore.Qt.AlignRight)
        self.setLayout(layout)
