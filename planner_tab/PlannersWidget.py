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
        self.planners_box = PlannersBox("Pick Planners")
        self.control_box = ControlBox("Control Options")
        self.option_box = OptionBox("Planner Options")
        self.reset_button = QtGui.QPushButton('Reset')
        
        layout = QtGui.QGridLayout()
        layout.addWidget(self.planners_box, 0, 0, 1, 2)
        layout.addWidget(self.control_box, 1, 0, 1, 2)
        layout.addWidget(self.option_box, 2, 0, 1, 2)
        layout.addWidget(self.reset_button, 3, 1, QtCore.Qt.AlignRight)
        self.setLayout(layout)

        self.reset_button.clicked.connect(self.reset)

    def reset(self):
        self.control_box.set_defaults()
        self.option_box.set_defaults()
        self.planners_box.set_defaults()

    def get_selected_planners(self):
        return self.planners_box.get_selected_planners()

    def get_time_limit(self):
        return self.control_box.get_time_limit()
    
    def get_propagation(self):
        return self.control_box.get_propagation()

    def get_max_control_duration(self):
        return self.control_box.get_max_control_duration()

    def get_min_control_duration(self):
        return self.control_box.get_min_control_duration()

    def get_planner_options(self):
        return self.option_box.get_options()