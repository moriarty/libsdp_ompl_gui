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

UPPER_BOUNDS = [10.0, 10.0]
LOWER_BOUNDS = [-10.0, -10.0]

# BoundsWidget class 

class BoundsWidget(QtGui.QWidget):
    def __init__(self):
        super(BoundsWidget, self).__init__()
        self.bounds_high = BoundsBox('Upper bounds')
        self.bounds_low = BoundsBox('Lower bounds')
        self.bounds_high.set_bounds(UPPER_BOUNDS)
        self.bounds_low.set_bounds(LOWER_BOUNDS)
        self.reset_button = QtGui.QPushButton('Reset')
        layout = QtGui.QGridLayout()
        layout.addWidget(self.bounds_high, 0, 0, 1, 2 )
        layout.addWidget(self.bounds_low, 1, 0, 1, 2)
        layout.addWidget(self.reset_button, 2, 1, QtCore.Qt.AlignRight)
        self.setLayout(layout)

    def reset(self):
        self.bounds_high.set_bounds(UPPER_BOUNDS)
        self.bounds_low.set_bounds(LOWER_BOUNDS)

    def get_bounds(self):
        upper = self.bounds_high.get_bounds()
        lower = self.bounds_low.get_bounds()
        return [upper, lower]
