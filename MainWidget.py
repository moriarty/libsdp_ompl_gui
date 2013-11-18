#!/usr/bin/env python
"""
# Title: MainWidget
# Description: QWidget to contain and arrange all of our widgets
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4 import QtGui
from plot_view import MPLViewer
from ProblemWidget import ProblemWidget
from BoundsWidget import BoundsWidget
from SolveWidget import SolveWidget
from PlannersWidget import PlannersWidget

class MainWidget(QtGui.QWidget):
     """docstring for MainWidget"""
     def __init__(self):
        super(MainWidget, self).__init__()
        self.mplViewer = MPLViewer()
        self.problemWidget = ProblemWidget()
        self.plannersWidget = PlannersWidget()
        self.boundsWidget = BoundsWidget()
        self.solveWidget = SolveWidget()
        #self.solveWidget.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed))
        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(self.problemWidget, "Problem")
        tabWidget.addTab(self.plannersWidget, "Planners")
        tabWidget.addTab(self.boundsWidget, "Bounding box")
        tabWidget.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed))
        layout = QtGui.QGridLayout()
        layout.addWidget(self.mplViewer, 0, 0, 2, 1)
        layout.addWidget(tabWidget, 0, 1)
        layout.addWidget(self.solveWidget, 2, 0, 1, 2)
        self.setLayout(layout)
        #self.problemWidget.startChanged.connect(self.glViewer.setStartPose)
        #self.problemWidget.goalChanged.connect(self.glViewer.setGoalPose)
        #self.solveWidget.explorationVizSelect.currentIndexChanged[int].connect(self.glViewer.showPlannerData)
        #self.solveWidget.animateCheck.toggled.connect(self.glViewer.toggleAnimation)
        #self.solveWidget.speedSlider.valueChanged.connect(self.glViewer.setSpeed)
