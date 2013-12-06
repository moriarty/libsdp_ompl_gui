#!/usr/bin/env python
"""
# Title: ObstacleWidget
# Description: ObstacleWidget is to set an Obstacle
# Author: @moriarty, @amdshameer
# Licence:
"""
# import statement

from PyQt4 import QtGui, QtCore
from ompl_gui.obstacle_tab.shapes import Square
from PyQt4.QtCore import pyqtSignal as Signal
from .. import Pose2DBox

# ObstacleWidget class

class ObstacleWidget(QtGui.QWidget):
    location_changed = Signal(list)
    def __init__(self):
        super(ObstacleWidget, self).__init__()
        self.obstacle_type_label = QtGui.QLabel('Obstacle Shape')
        self.obstacle_type_select = QtGui.QComboBox()
        self.obstacle_type_select.addItem("Square")
        self.obstacle_type_select.addItem("None")
        
        self.obstacle = Square("Square")

        self.obstacle_pose = Pose2DBox('Obstacle Centre')
        self.obstacle_pose.yaw.setEnabled(False)

        layout = QtGui.QGridLayout()
        layout.addWidget(
            self.obstacle_type_label, 0, 0, QtCore.Qt.AlignLeft)
        layout.addWidget(
            self.obstacle_type_select, 0, 1, QtCore.Qt.AlignRight)
        layout.addWidget(
            self.obstacle, 1, 0, 1, 2, QtCore.Qt.AlignTop)
        layout.addWidget(
            self.obstacle_pose, 2, 0, 1, 2, QtCore.Qt.AlignTop)
        self.setLayout(layout)

        self.obstacle_pose.value_changed.connect(self.location_change)

    def get_obstacle_info(self):
        info = {}
        info.update({"type": self.get_type()})
        info.update({"location": self.get_location()})
        info.update(self.obstacle.get_info())
        return info

    def get_type(self):
        return str(self.obstacle_type_select.currentText())

    def get_location(self):
        return self.obstacle_pose.get_pose()[0:2]

    def location_change(self):
        self.location_changed.emit(self.get_location())

