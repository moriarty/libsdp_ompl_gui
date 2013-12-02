#!/usr/bin/env python
"""
# Title: PlannersWidget
# Description: QWidget for setting Planner information
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4 import QtGui, QtCore

from ompl_gui.planner_tab.PlannersBox import PlannersBox
from ompl_gui.planner_tab.ControlBox import ControlBox
from ompl_gui.planner_tab.OptionBox import OptionBox

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
        
        layout = QtGui.QGridLayout()
        layout.addWidget(self.plannersBox, 0, 0, 1, 2)
        layout.addWidget(self.controlBox, 1, 0, 1, 2)
        layout.addWidget(self.optionBox, 2, 0, 1, 2)
        layout.addWidget(self.resetButton, 3, 1, QtCore.Qt.AlignRight)
        self.setLayout(layout)

        self.resetButton.clicked.connect(self.reset)

    def reset(self):
        self.controlBox.setDefaults()
        self.optionBox.setDefaults()
        self.plannersBox.setDefaults()

    def getSelectedPlanners(self):
        return self.plannersBox.getSelectedPlanners()

    def getTimeLimit(self):
        return self.controlBox.getTimeLimit()
    
    def getPropagation(self):
        return self.controlBox.getPropagation()

    def getMaxControlDuration(self):
        return self.controlBox.getMaxControlDuration()

    def getMinControlDuration(self):
        return self.controlBox.getMinControlDuration()

    def getPlannerOptions(self):
        return self.optionBox.getOptions()