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
        self.problem_widget = ProblemWidget()
        self.plannersWidget = PlannersWidget()
        self.obstacleWidget = ObstacleWidget()
        self.bounds_widget = BoundsWidget()
        self.solve_widget = SolveWidget()
        
        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(self.problem_widget, "Problem")
        tabWidget.addTab(self.plannersWidget, "Planners")
        tabWidget.addTab(self.bounds_widget, "Bounding box")
        tabWidget.addTab(self.obstacleWidget, "Obstacle")
        tabWidget.setTabEnabled(3, False)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.mplViewer, 0, 0, 2, 1)
        layout.addWidget(tabWidget, 0, 1)
        layout.addWidget(self.solve_widget, 2, 0, 1, 2)
        self.setLayout(layout)

        self.solve_widget.clear_button.clicked.connect(
            self.mplViewer.clear)
        self.solve_widget.reset_button.clicked.connect(
            self.reset)

        ## Bounds Widget and Path Viewer MPL.
        ## Connections are very loopy atm
        self.bounds_widget.reset_button.clicked.connect(
            self.mplViewer.resetBounds)
        self.bounds_widget.bounds_low.value_changed.connect(
            self.mplViewer.setLowerBounds)
        self.bounds_widget.bounds_high.value_changed.connect(
            self.mplViewer.setUpperBounds)

    def reset(self):
        self.problem_widget.reset()
        self.plannersWidget.reset()
        self.bounds_widget.reset()

    def get_bounds(self):
        return self.bounds_widget.get_bounds()

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

    def enable_plot_button(self, set_enabled=True):
        return self.solve_widget.enable_plot_button(set_enabled=set_enabled)
    
    def enable_plans_button(self, set_enabled=True):
        return self.solve_widget.enable_plans_button(set_enabled=set_enabled)
    
    def get_start_pose(self):
        return self.problem_widget.get_start_pose()

    def get_goal_pose(self):
        return self.problem_widget.get_goal_pose()
