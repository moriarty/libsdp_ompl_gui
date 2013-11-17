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
        self.resetButton = QtGui.QPushButton('Reset')
        self.applyButton = QtGui.QPushButton('Apply')
        
        layout = QtGui.QGridLayout()
        layout.addWidget(self.plannersBox,0,0,1,2)
        layout.addWidget(self.controlBox,1,0,1,2)
        layout.addWidget(self.optionBox, 2, 0,1,2)
        layout.addWidget(self.resetButton,3,0, QtCore.Qt.AlignRight)
        layout.addWidget(self.applyButton,3,1, QtCore.Qt.AlignRight)
        self.setLayout(layout)

        self.resetButton.clicked.connect(self.plannersBox.setDefaults)
        self.resetButton.clicked.connect(self.controlBox.setDefaults)
        self.resetButton.clicked.connect(self.optionBox.setDefaults)

    def getTimeLimit(self):
        return self.controlBox.getTimeLimit()
    
    def getPropagation(self):
        return self.controlBox.getPropagation()

    def getMaxControlDuration(self):
        return self.controlBox.getMaxControlDuration()

    def getMinControlDuration(self):
        return self.controlBox.getMinControlDuration()