#!/usr/bin/env python
"""
# Title: Pose2DBox
# Description: Pose2DBox to set the X,Y,Yaw
# Author: @moriarty, @amdshameer
# Licence: 
"""
# import statement
from PyQt4 import QtCore, QtGui

# Pose2DBox class
class Pose2DBox(QtGui.QGroupBox):
    valueChanged = Signal(list)

    def __init__(self, title):
        super(Pose2DBox, self).__init__(title)
        xlabel = QtGui.QLabel('X')
        ylabel = QtGui.QLabel('Y')
        rotlabel = QtGui.QLabel('Rotation')

        self.posx = QtGui.QDoubleSpinBox()
        self.posx.setRange(-1000, 1000)
        self.posx.setSingleStep(1)
        self.posy = QtGui.QDoubleSpinBox()
        self.posy.setRange(-1000, 1000)
        self.posy.setSingleStep(1)
        self.rot = QtGui.QDoubleSpinBox()
        self.rot.setRange(-360,360)
        self.rot.setSingleStep(1)

        layout = QtGui.QGridLayout()
        layout.addWidget(xlabel, 0, 0, QtCore.Qt.AlignRight)
        layout.addWidget(ylabel, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(rotlabel, 2, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.posx, 0, 1)
        layout.addWidget(self.posy, 1, 1)
        layout.addWidget(self.rot, 2, 1)
        self.setLayout(layout)

        self.posx.valueChanged.connect(self.poseChange)
        self.posy.valueChanged.connect(self.poseChange)
        self.rot.valueChanged.connect(self.poseChange)

    def setPose(self, value):
        state = value()
        self.posx.setValue(state.getX())
        self.posy.setValue(state.getY())
        self.rot.setValue(state.getYaw() * 180 / pi)

    def getPose(self):
        state = ob.State(ob.SE2StateSpace())
        state().setX(self.posx.value())
        state().setY(self.posy.value())
        state().setYaw(self.rot.value() * pi / 180)
        return state

    def poseChange(self, value):
        self.valueChanged.emit([0, 0, self.rot.value(), self.posx.value(), self.posy.value(), 0 ])