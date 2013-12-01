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

        rangeLabel = QtGui.QLabel('Range')
        self.rangeBox = QtGui.QDoubleSpinBox()
        self.rangeBox.setRange(0, 100)
        self.rangeBox.setSingleStep(1.00)
        self.rangeBox.setValue(0.00)

        borderFractionLabel = QtGui.QLabel('Border Fraction')
        self.borderFraction = QtGui.QDoubleSpinBox()
        self.borderFraction.setRange(0, 1)
        self.borderFraction.setSingleStep(0.05)
        self.borderFraction.setValue(0.80) 

        layout = QtGui.QGridLayout()
        layout.addWidget(goalBiasLabel, 0, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.goalBias, 0, 1, 1, 2)
        layout.addWidget(rangeLabel, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.rangeBox, 1, 1, 1, 2)
        layout.addWidget(borderFractionLabel, 2, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.borderFraction, 2, 1, 1, 2)
        self.setLayout(layout)

    def setGoalBias(self, value=0.05):
        self.goalBias.setValue(value)

    def setBorderFraction(self, value=0.80):
        self.borderFraction.setValue(value)

    def setRange(self, value=0.00):
        self.rangeBox.setValue(value)

    def setDefaults(self):
        self.setGoalBias()
        self.setBorderFraction()
        self.setRange()

    def getGoalBias(self):
        return self.goalBias.value()

    def getRange(self):
        return self.rangeBox.value()

    def getBorderFraction(self):
        return self.borderFraction.value()

    def getOptions(self):
        options = {}
        options.update({"goal_bias": self.getGoalBias()})
        options.update({"range": self.getRange()})
        options.update({"border_fraction": self.getBorderFraction()})
        return options


