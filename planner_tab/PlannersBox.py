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
    """docstring for PlannersBox"""
    def __init__(self, title):
        super(PlannersBox, self).__init__(title)
        
        # RRT, PDST 
        self.rrtCheck = QtGui.QCheckBox('RRT (default)')
        self.rrtCheck.setChecked(True)
        self.pdstCheck = QtGui.QCheckBox('PDST')
        self.pdstCheck.setChecked(False)
        # EST, KPIECE1
        self.estCheck = QtGui.QCheckBox('EST')
        self.estCheck.setChecked(False)
        self.estCheck.setEnabled(False)
        self.kpiece1Check = QtGui.QCheckBox('KPIECE1')
        self.kpiece1Check.setChecked(False)
        self.kpiece1Check.setEnabled(False)

        self.planners = []
        self.planners.append([self.rrtCheck, "RRT"])
        self.planners.append([self.pdstCheck, "PDST"])
        self.planners.append([self.estCheck, "EST"])
        self.planners.append([self.kpiece1Check, "KPIECE1"])

        layout = QtGui.QGridLayout()
        layout.addWidget(self.rrtCheck, 0, 0)
        layout.addWidget(self.pdstCheck, 0, 1)
        layout.addWidget(self.estCheck, 1, 0)
        layout.addWidget(self.kpiece1Check,1,1)
        self.setLayout(layout)

        # Connect buttons to insure at least one is selected.
        self.rrtCheck.stateChanged.connect(self.ensurePlanner)
        self.pdstCheck.stateChanged.connect(self.ensurePlanner)
        self.estCheck.stateChanged.connect(self.ensurePlanner)
        self.kpiece1Check.stateChanged.connect(self.ensurePlanner)

    def getSelectedPlanners(self):
        selectedPlanners = []
        for plannerCheck, name in self.planners:
            if plannerCheck.checkState():
                selectedPlanners.append(name)
        return selectedPlanners

    def ensurePlanner(self):
        """
        Note: I've tried this many different ways, but there is still a bug.
        Double checking RRT does not recheck RRT, 
        """
        if self.rrtCheck.checkState(): 
            pass
        elif self.pdstCheck.checkState(): 
            pass
        elif self.estCheck.checkState(): 
            pass
        elif self.kpiece1Check.checkState(): 
            pass
        else:
            self.setDefaults()

    def setDefaults(self):
        """Sets the RRT to checked"""
        self.rrtCheck.setChecked(True)
        self.pdstCheck.setChecked(False)
        self.estCheck.setChecked(False)
        self.kpiece1Check.setChecked(False)

