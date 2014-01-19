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
    """For changing the values of the planner parameters"""
    def __init__(self, title):
        super(OptionBox, self).__init__(title)
        
        goal_bias_label = QtGui.QLabel('Goal bias')
        self.goal_bias = QtGui.QDoubleSpinBox()
        self.goal_bias.setRange(0, 1)
        self.goal_bias.setSingleStep(0.05)
        self.goal_bias.setValue(0.05)

        range_label = QtGui.QLabel('Range')
        self.range_box = QtGui.QDoubleSpinBox()
        self.range_box.setRange(0, 100)
        self.range_box.setSingleStep(1.00)
        self.range_box.setValue(0.00)

        border_fraction_label = QtGui.QLabel('Border Fraction')
        self.border_fraction = QtGui.QDoubleSpinBox()
        self.border_fraction.setRange(0, 1)
        self.border_fraction.setSingleStep(0.05)
        self.border_fraction.setValue(0.80) 

        layout = QtGui.QGridLayout()
        layout.addWidget(goal_bias_label, 0, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.goal_bias, 0, 1, 1, 2)
        layout.addWidget(range_label, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.range_box, 1, 1, 1, 2)
        layout.addWidget(border_fraction_label, 2, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.border_fraction, 2, 1, 1, 2)
        self.setLayout(layout)

    def set_goal_bias(self, value=0.05):
        self.goal_bias.setValue(value)

    def set_border_fraction(self, value=0.80):
        self.border_fraction.setValue(value)

    def set_range(self, value=0.00):
        self.range_box.setValue(value)

    def set_defaults(self):
        self.set_goal_bias()
        self.set_border_fraction()
        self.set_range()

    def get_goal_bias(self):
        return self.goal_bias.value()

    def get_range(self):
        return self.range_box.value()

    def get_border_fraction(self):
        return self.border_fraction.value()

    def get_options(self):
        options = {}
        options.update({"goal_bias": self.get_goal_bias()})
        options.update({"range": self.get_range()})
        options.update({"border_fraction": self.get_border_fraction()})
        return options


