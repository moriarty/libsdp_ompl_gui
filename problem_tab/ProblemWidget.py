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
    start_changed = Signal(list)
    goal_changed = Signal(list)

    def __init__(self):
        super(ProblemWidget, self).__init__()
        robot_type_label = QtGui.QLabel('Robot type')
        self.robot_type_select = QtGui.QComboBox()
        self.robot_type_select.addItem("K. Car 2D")
        self.robot_type_select.setMaximumSize(200, 2000)

        self.start_pose = Pose2DBox('Start pose')
        self.goal_pose = Pose2DBox('Goal pose')
        self.reset_button = QtGui.QPushButton('Reset')

        layout = QtGui.QGridLayout()
        layout.addWidget(robot_type_label, 0, 0,
            QtCore.Qt.AlignTop)
        layout.addWidget(self.robot_type_select, 0, 1,
            QtCore.Qt.AlignTop)
        layout.addWidget(self.start_pose, 1, 0, 1, 2)
        layout.addWidget(self.goal_pose, 2, 0, 1, 2)
        layout.addWidget(self.reset_button, 3, 1, QtCore.Qt.AlignRight)
        self.setLayout(layout)

        self.reset_button.clicked.connect(self.reset)

        self.start_pose.valueChanged.connect(self.start_pose_change)
        self.goal_pose.valueChanged.connect(self.goal_pose_change)

    def reset(self):
        self.set_start_pose()
        self.set_goal_pose()

    def set_start_pose(self, x=0.0, y=0.0, yaw=0.0):
        self.start_pose.setPose(x=x, y=y, yaw=yaw)
    def set_goal_pose(self, x=0.0, y=0.0, yaw=0.0):
        self.goal_pose.setPose(x=x, y=y, yaw=yaw)

    def get_start_pose(self):
        return self.start_pose.getPose()
    def get_goal_pose(self):
        return self.goal_pose.getPose()

    def start_pose_change(self, value):
        self.start_changed.emit(value)
    def goal_pose_change(self, value):
        self.goal_changed.emit(value)
