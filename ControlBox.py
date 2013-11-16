#!/usr/bin/env python
"""
# Title:ControlBox
# Description: QGroupBox for holding control options
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal as Signal

class ControlBox(QtGui.QGroupBox):
    """docstring for ControlBox"""
    def __init__(self, title):
        super(ControlBox, self).__init__(title)
        
        timeLimitLabel = QtGui.QLabel('Time (sec.)')
        self.timeLimit = QtGui.QDoubleSpinBox()
        self.timeLimit.setRange(0, 100)
        self.timeLimit.setSingleStep(1)
        self.timeLimit.setValue(5.0)

        propagationLabel = QtGui.QLabel('Propagation\nstep size')
        propagationLabel.setAlignment(QtCore.Qt.AlignRight)
        self.propagation = QtGui.QDoubleSpinBox()
        self.propagation.setRange(0.01, 1000.00)
        self.propagation.setSingleStep(.01)
        self.propagation.setValue(0.2)
        self.propagation.setDecimals(2)

        durationLabel = QtGui.QLabel('Control duration\n(min/max #steps)')
        durationLabel.setAlignment(QtCore.Qt.AlignRight)
        self.minControlDuration = QtGui.QSpinBox()
        self.minControlDuration.setRange(1, 1000)
        self.minControlDuration.setSingleStep(1)
        self.minControlDuration.setValue(1)
        self.maxControlDuration = QtGui.QSpinBox()
        self.maxControlDuration.setRange(1, 1000)
        self.maxControlDuration.setSingleStep(1)
        self.maxControlDuration.setValue(20)

        layout = QtGui.QGridLayout()
        layout.addWidget(timeLimitLabel, 0, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.timeLimit, 0, 1, 1, 2)
        layout.addWidget(propagationLabel, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.propagation, 1, 1, 1, 2)
        layout.addWidget(durationLabel, 2, 0)
        layout.addWidget(self.minControlDuration, 2, 1)
        layout.addWidget(self.maxControlDuration, 2, 2)
        self.setLayout(layout)

    def setTimeLimit(self, value=5.0):
        self.timeLimit(value)

    def setPropagation(self, value=0.2):
        self.propagation.setValue(value)

    def setMinControlDuration(self, value=1):
        self.minControlDuration.setValue(value)

    def setMaxControlDuration(self, value=20):
        self.maxControlDuration.setValue(value)

    def setDefaults(self):
        self.setTimeLimit()
        self.setPropagation()
        self.setMinControlDuration()
        self.setMaxControlDuration()

