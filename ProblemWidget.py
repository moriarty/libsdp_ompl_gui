#!/usr/bin/env python
"""
# Title: ProblemWidget
# Description: a QtGui Widget to define the Demo Problem
# The Problem definition contains start and goal positions. 
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal as Signal
from Pose2DBox import Pose2DBox

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


        self.startPose2D = Pose2DBox('Start pose')
        self.goalPose2D = Pose2DBox('Goal pose')

        startGoal2D = QtGui.QWidget()
        layout = QtGui.QGridLayout()
        layout.addWidget(self.startPose2D, 0, 0, 1, 2)
        layout.addWidget(self.goalPose2D, 1, 0, 1 ,2)
        startGoal2D.setLayout(layout)

        self.poses = QtGui.QStackedWidget()
        self.poses.addWidget(startGoal2D)

        layout = QtGui.QGridLayout()
        layout.addWidget(robotTypeLabel, 0, 0)
        layout.addWidget(self.robotTypeSelect, 0, 1)
        layout.addWidget(self.poses, 1, 0, 1, 2)
        self.setLayout(layout)

        self.startPose2D.valueChanged.connect(self.startPoseChange)
        self.goalPose2D.valueChanged.connect(self.goalPoseChange)

    def setStartPose(self, value):
        self.startPose2D.setPose(value)
    def setGoalPose(self, value):
        self.goalPose2D.setPose(value)

    def getStartPose(self):
        return self.startPose3D.getPose() if self.poses.currentIndex()==0 else self.startPose2D.getPose()
    def getGoalPose(self):
        return self.goalPose3D.getPose() if self.poses.currentIndex()==0 else self.goalPose2D.getPose()

    def startPoseChange(self, value):
        self.startChanged.emit(value)
    def goalPoseChange(self, value):
        self.goalChanged.emit(value)
