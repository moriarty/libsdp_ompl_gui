#!/usr/bin/env python
"""
# Title:ControlBox
# Description: QGroupBox for holding control options
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement
from PyQt4 import QtCore, QtGui

class ControlBox(QtGui.QGroupBox):
    """docstring for ControlBox"""
    def __init__(self, title):
        super(ControlBox, self).__init__(title)
        
        time_limit_label = QtGui.QLabel('Time (sec.)')
        self.time_limit = QtGui.QDoubleSpinBox()
        self.time_limit.setRange(0, 100)
        self.time_limit.setSingleStep(1)
        self.time_limit.setValue(5.0)

        propagation_label = QtGui.QLabel('Propagation\nstep size')
        propagation_label.setAlignment(QtCore.Qt.AlignRight)
        self.propagation = QtGui.QDoubleSpinBox()
        self.propagation.setRange(0.01, 1000.00)
        self.propagation.setSingleStep(.01)
        self.propagation.setValue(0.2)
        self.propagation.setDecimals(2)

        duration_label = QtGui.QLabel('Control duration\n(min/max #steps)')
        duration_label.setAlignment(QtCore.Qt.AlignRight)
        self.min_control_duration = QtGui.QSpinBox()
        self.min_control_duration.setRange(1, 1000)
        self.min_control_duration.setSingleStep(1)
        self.min_control_duration.setValue(1)
        self.max_control_duration = QtGui.QSpinBox()
        self.max_control_duration.setRange(1, 1000)
        self.max_control_duration.setSingleStep(1)
        self.max_control_duration.setValue(20)

        layout = QtGui.QGridLayout()
        layout.addWidget(time_limit_label, 0, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.time_limit, 0, 1, 1, 2)
        layout.addWidget(propagation_label, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.propagation, 1, 1, 1, 2)
        layout.addWidget(duration_label, 2, 0)
        layout.addWidget(self.min_control_duration, 2, 1)
        layout.addWidget(self.max_control_duration, 2, 2)
        self.setLayout(layout)

    def get_time_limit(self):
        return self.time_limit.value()

    def get_propagation(self):
        return self.propagation.value()

    def get_min_control_duration(self):
        return self.min_control_duration.value()

    def get_max_control_duration(self):
        return self.max_control_duration.value()

    def set_time_limit(self, value=5.0):
        self.time_limit.setValue(value)

    def set_propagation(self, value=0.2):
        self.propagation.setValue(value)

    def set_min_control_duration(self, value=1):
        self.min_control_duration.setValue(value)

    def set_max_control_duration(self, value=20):
        self.max_control_duration.setValue(value)

    def set_defaults(self):
        self.set_time_limit()
        self.set_propagation()
        self.set_min_control_duration()
        self.set_max_control_duration()

