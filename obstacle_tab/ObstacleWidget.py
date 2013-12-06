#!/usr/bin/env python
"""
# Title: ObstacleWidget
# Description: ObstacleWidget is to set an Obstacle
# Author: @moriarty, @amdshameer
# Licence:
"""
# import statement

from PyQt4 import QtGui
from ompl_gui.obstacle_tab.shapes import Square
from .. import Pose2DBox

# ObstacleWidget class

class ObstacleWidget(QtGui.QWidget):
    def __init__(self):
        super(ObstacleWidget, self).__init__()
        self.obstacle_type_label = QtGui.QLabel('Obstacle Shape')
        self.obstacle_type_select = QtGui.QComboBox()
        self.obstacle_type_select.addItem("Square")
        
        self.obstacle_pose = Pose2DBox('Obstacle Centre')
        self.obstacle_pose.yaw.setEnabled(False)

        self.obstacle = self.obstacle_type_select

        layout = QtGui.QGridLayout()
        layout.addWidget(self.obstacle_type_label, 0, 0)
        layout.addWidget(self.obstacle_type_select, 0, 1)
        layout.addWidget(self.obstacle_pose, 1, 0, 1, 2)
        self.setLayout(layout)
