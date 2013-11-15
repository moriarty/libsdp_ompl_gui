#!/usr/bin/env python
"""
# Title:PlannersBox
# Description: QGroupBox for holding planners to be choosen from
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal as Signal

class PlannersBox(QtGui.QGroupBox):
    """docstring for PlannersBox"""
    def __init__(self, title):
        super(PlannersBox, self).__init__(title)
        
        # RRT, PDST 
        self.rrtCheck = QtGui.QCheckBox('RRT')
        self.rrtCheck.setChecked(True)
        self.pdstCheck = QtGui.QCheckBox('PDST')
        self.pdstCheck.setChecked(False)
        # EST, KPIECE1
        self.estCheck = QtGui.QCheckBox('RRT')
        self.estCheck.setChecked(False)
        self.estCheck.setEnabled(False)
        self.kpiece1Check = QtGui.QCheckBox('PDST')
        self.kpiece1Check.setChecked(False)
        self.kpiece1Check.setEnabled(False)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.rrtCheck, 0, 0)
        layout.addWidget(self.pdstCheck, 0, 1)
        layout.addWidget(self.estCheck, 1, 0)
        layout.addWidget(self.kpiece1Check,1,1)
        self.setLayout(layout)
