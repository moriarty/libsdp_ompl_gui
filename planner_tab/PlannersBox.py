#!/usr/bin/env python
"""
# Title:PlannersBox
# Description: QGroupBox for holding planners to be choosen from
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement
from PyQt4 import QtGui

class PlannersBox(QtGui.QGroupBox):
    """This helps in selecting a list of planners. RRT is set as default"""
    def __init__(self, title):
        super(PlannersBox, self).__init__(title)
        
        self.rrt_check = QtGui.QCheckBox('RRT (default)')
        self.rrt_check.setChecked(True)
        self.pdst_check = QtGui.QCheckBox('PDST')
        self.pdst_check.setChecked(False)
        self.est_check = QtGui.QCheckBox('EST')
        self.est_check.setChecked(False)
        self.kpiece1_check = QtGui.QCheckBox('KPIECE1')
        self.kpiece1_check.setChecked(False)
        
        self.planners = []
        self.planners.append([self.rrt_check, "RRT"])
        self.planners.append([self.pdst_check, "PDST"])
        self.planners.append([self.est_check, "EST"])
        self.planners.append([self.kpiece1_check, "KPIECE1"])

        layout = QtGui.QGridLayout()
        layout.addWidget(self.rrt_check, 0, 0)
        layout.addWidget(self.pdst_check, 0, 1)
        layout.addWidget(self.est_check, 1, 0)
        layout.addWidget(self.kpiece1_check, 1, 1)
        self.setLayout(layout)

        # Connect buttons to insure at least one is selected.
        self.rrt_check.stateChanged.connect(self.ensure_planner)
        self.pdst_check.stateChanged.connect(self.ensure_planner)
        self.est_check.stateChanged.connect(self.ensure_planner)
        self.kpiece1_check.stateChanged.connect(self.ensure_planner)

    def get_selected_planners(self):
        selected_planners = []
        for planner_check, name in self.planners:
            if planner_check.checkState():
                selected_planners.append(name)
        return selected_planners

    def ensure_planner(self):
        """
        Note: I've tried this many different ways, but there is still a bug.
        Double checking RRT does not recheck RRT, 
        """
        if self.rrt_check.checkState(): 
            pass
        elif self.pdst_check.checkState(): 
            pass
        elif self.est_check.checkState(): 
            pass
        elif self.kpiece1_check.checkState(): 
            pass
        else:
            self.set_defaults()

    def set_defaults(self):
        """Sets the RRT to checked"""
        self.rrt_check.setChecked(True)
        self.pdst_check.setChecked(False)
        self.est_check.setChecked(False)
        self.kpiece1_check.setChecked(False)

