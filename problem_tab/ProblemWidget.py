#!/usr/bin/env python
"""
# Title: ProblemWidget
# Description: a QtGui Widget to define the Demo Problem
# The Problem definition contains start and goal positions. 
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal as Signal
from .. import Pose2DBox

class ProblemWidget(QtGui.QWidget):
    """docstring for ProblemWidget"""
    startChanged = Signal(list)
    goalChanged = Signal(list)

    def __init__(self):
        super(ProblemWidget, self).__init__()
        robotTypeLabel = QtGui.QLabel('Robot type')
        self.robotTypeSelect = QtGui.QComboBox()
        self.robotTypeSelect.addItem("K.CarDemo2D")
        self.robotTypeSelect.setMaximumSize(200, 2000)

        self.startPose = Pose2DBox('Start pose')
        self.goalPose = Pose2DBox('Goal pose')
        self.resetButton = QtGui.QPushButton('Reset')

        layout = QtGui.QGridLayout()
        layout.addWidget(robotTypeLabel, 0, 0)
        layout.addWidget(self.robotTypeSelect, 0, 1)
        layout.addWidget(self.startPose, 1, 0, 1, 2)
        layout.addWidget(self.goalPose, 2, 0, 1 ,2)
        layout.addWidget(self.resetButton, 3,1, QtCore.Qt.AlignRight)
        self.setLayout(layout)

        self.startPose.valueChanged.connect(self.startPoseChange)
        self.goalPose.valueChanged.connect(self.goalPoseChange)

    def setStartPose(self, x=0.0, y=0.0, yaw=0.0):
        self.startPose.setPose(x=x, y=y, yaw=yaw)
    def setGoalPose(self, x=0.0, y=0.0, yaw=0.0):
        self.goalPose.setPose(x=x, y=y, yaw=yaw)

    def getStartPose(self):
        return self.startPose.getPose()
    def getGoalPose(self):
        return self.goalPose.getPose()

    def startPoseChange(self, value):
        self.startChanged.emit(value)
    def goalPoseChange(self, value):
        self.goalChanged.emit(value)
