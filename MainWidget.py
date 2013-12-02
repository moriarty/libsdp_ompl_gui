#!/usr/bin/env python
"""
# Title: MainWidget
# Description: QWidget to contain and arrange all of our widgets
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4 import QtGui
from ompl_gui.plot_view import MPLViewer
from ompl_gui.problem_tab import ProblemWidget
from ompl_gui.bounds_tab import BoundsWidget
from ompl_gui.SolveWidget import SolveWidget
from ompl_gui.planner_tab import PlannersWidget
from ompl_gui.obstacle_tab import ObstacleWidget

class MainWidget(QtGui.QWidget):
    """Main Widget
    A QWidget which contains the graphical plan viewer,
    tabs for configuring the planners and controls to solve and plot 
    """
    def __init__(self):
        super(MainWidget, self).__init__()
        self.mplViewer = MPLViewer()
        self.problemWidget = ProblemWidget()
        self.plannersWidget = PlannersWidget()
        self.obstacleWidget = ObstacleWidget()
        self.boundsWidget = BoundsWidget()
        self.solveWidget = SolveWidget()
        
        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(self.problemWidget, "Problem")
        tabWidget.addTab(self.plannersWidget, "Planners")
        tabWidget.addTab(self.boundsWidget, "Bounding box")
        tabWidget.addTab(self.obstacleWidget, "Obstacle")
        tabWidget.setTabEnabled(3, False)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.mplViewer, 0, 0, 2, 1)
        layout.addWidget(tabWidget, 0, 1)
        layout.addWidget(self.solveWidget, 2, 0, 1, 2)
        self.setLayout(layout)

        self.solveWidget.clearButton.clicked.connect(
            self.mplViewer.clear)
        self.solveWidget.resetButton.clicked.connect(
            self.reset)

        ## Bounds Widget and Path Viewer MPL.
        ## Connections are very loopy atm
        self.boundsWidget.resetButton.clicked.connect(
            self.mplViewer.resetBounds)
        self.boundsWidget.bounds_low.valueChanged.connect(
            self.mplViewer.setLowerBounds)
        self.boundsWidget.bounds_high.valueChanged.connect(
            self.mplViewer.setUpperBounds)

    def reset(self):
        self.problemWidget.reset()
        self.plannersWidget.reset()
        self.boundsWidget.reset()

    def getBounds(self):
        return self.boundsWidget.getBounds()

    def getSelectedPlanners(self):
        return self.plannersWidget.getSelectedPlanners()
    
    def getPropagation(self):
        return self.plannersWidget.getPropagation()
    
    def getMinControlDuration(self):
        return self.plannersWidget.getMinControlDuration()
    
    def getMaxControlDuration(self):
        return self.plannersWidget.getMaxControlDuration()
    
    def getPlannerOptions(self):
        return self.plannersWidget.getPlannerOptions()
    
    def getTimeLimit(self):
        return self.plannersWidget.getTimeLimit()

    def enablePlotButton(self, setEnabled=True):
        return self.solveWidget.enablePlotButton(setEnabled=setEnabled)
    
    def enablePlansButton(self, setEnabled=True):
        return self.solveWidget.enablePlansButton(setEnabled=setEnabled)
        
