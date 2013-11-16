#!/usr/bin/env python
"""
# Title: PlannersWidget
# Description: QWidget for setting Planner information
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4 import QtGui, QtCore

from PlannersBox import PlannersBox
from ControlBox import ControlBox
from OptionBox import OptionBox

class PlannersWidget(QtGui.QWidget):
    """PlannersWidget
    A QWidget which contains all planner settings
    """
    def __init__(self):
        super(PlannersWidget, self).__init__()
        self.plannersBox = PlannersBox("Pick Planners")
        self.controlBox = ControlBox("Control Options")
        self.optionBox = OptionBox("Planner Options")
        
        layout = QtGui.QGridLayout()
        layout.addWidget(self.plannersBox,0,0)
        layout.addWidget(self.controlBox,1,0)
        layout.addWidget(self.optionBox, 2, 0)
        self.setLayout(layout)
       
