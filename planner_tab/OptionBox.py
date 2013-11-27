#!/usr/bin/env python
"""
# Title:OptionBox
# Description: QGroupBox for holding planner options
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement
from PyQt4 import QtCore, QtGui

class OptionBox(QtGui.QGroupBox):
    """docstring for OptionBox"""
    def __init__(self, title):
        super(OptionBox, self).__init__(title)
        
        goalBiasLabel = QtGui.QLabel('Goal bias')
        self.goalBias = QtGui.QDoubleSpinBox()
        self.goalBias.setRange(0, 1)
        self.goalBias.setSingleStep(0.05)
        self.goalBias.setValue(0.05)

        layout = QtGui.QGridLayout()
        layout.addWidget(goalBiasLabel, 0, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.goalBias, 0, 1, 1, 2)
        self.setLayout(layout)

    def setGoalBias(self, value=0.05):
        self.goalBias.setValue(value)

    def setDefaults(self):
        self.setGoalBias()

