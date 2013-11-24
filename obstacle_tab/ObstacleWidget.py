#!/usr/bin/env python
"""
# Title: ObstacleWidget
# Description: ObstacleWidget is to set an Obstacle
# Author: @moriarty, @amdshameer
# Licence:
"""
# import statement

from PyQt4 import QtCore, QtGui
from shapes import Square
from .. import Pose2DBox

# ObstacleWidget class

class ObstacleWidget(QtGui.QWidget):
    def __init__(self):
        super(ObstacleWidget, self).__init__()
        self.obstacleTypeLabel = QtGui.QLabel('Obstacle Shape')
        self.obstacleTypeSelect = QtGui.QComboBox()
        
        self.obstaclePose = Pose2DBox('Obstacle Centre')
        self.obstaclePose.yaw.setEnabled(False)

        self.obstacle = self.obstacleTypeSelect

        self.applyButton = QtGui.QPushButton('Apply')

        layout = QtGui.QGridLayout()
        layout.addWidget(self.obstacleTypeLabel, 0,0)
        layout.addWidget(self.obstacleTypeSelect, 0,1)
        layout.addWidget(self.obstaclePose, 1, 0, 1, 2)
        layout.addWidget(self.applyButton, 2,0, QtCore.Qt.AlignRight)
        self.setLayout(layout)