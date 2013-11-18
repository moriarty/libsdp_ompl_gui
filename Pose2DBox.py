#!/usr/bin/env python
"""
# Title: Pose2DBox
# Description: Pose2DBox to set the X,Y,Yaw
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal as Signal
import numpy as np 

# Pose2DBox class
class Pose2DBox(QtGui.QGroupBox):
    valueChanged = Signal(list)

    def __init__(self, title):
        super(Pose2DBox, self).__init__(title)
        xlabel = QtGui.QLabel('X')
        ylabel = QtGui.QLabel('Y')
        yawlabel = QtGui.QLabel('Yaw (degree)')

        self.posx = QtGui.QDoubleSpinBox()
        self.posx.setRange(-100, 100)
        self.posx.setSingleStep(1)
        self.posy = QtGui.QDoubleSpinBox()
        self.posy.setRange(-100, 100)
        self.posy.setSingleStep(1)
        self.yaw = QtGui.QDoubleSpinBox()
        self.yaw.setRange(-360,360)
        self.yaw.setSingleStep(1)

        layout = QtGui.QGridLayout()
        layout.addWidget(xlabel, 0, 0, QtCore.Qt.AlignRight)
        layout.addWidget(ylabel, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(yawlabel, 2, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.posx, 0, 1)
        layout.addWidget(self.posy, 1, 1)
        layout.addWidget(self.yaw, 2, 1)
        self.setLayout(layout)

        self.posx.valueChanged.connect(self.poseChange)
        self.posy.valueChanged.connect(self.poseChange)
        self.yaw.valueChanged.connect(self.poseChange)

    def setPose(self, x=0, y=0, yaw=0):
        state = value()
        self.posx.setValue(x)
        self.posy.setValue(y)
        self.yaw.setValue(yaw * 180 / pi)

    def getPose(self):
        x = self.posx.value()
        y = self.posy.value()
        yaw = self.yaw.value()
        return [x, y, yaw]

    def poseChange(self):
        self.valueChanged.emit( self.getPose() )
