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
        self.mpl_viewer = MPLViewer()
        self.problem_widget = ProblemWidget()
        self.planners_widget = PlannersWidget()
        self.obstacle_widget = ObstacleWidget()
        self.bounds_widget = BoundsWidget()
        self.solve_widget = SolveWidget()
        
        tab_widget = QtGui.QTabWidget()
        tab_widget.addTab(self.problem_widget, "Problem")
        tab_widget.addTab(self.planners_widget, "Planners")
        tab_widget.addTab(self.bounds_widget, "Bounding box")
        tab_widget.addTab(self.obstacle_widget, "Obstacle")

        layout = QtGui.QGridLayout()
        layout.addWidget(self.mpl_viewer, 0, 0, 2, 1)
        layout.addWidget(tab_widget, 0, 1)
        layout.addWidget(self.solve_widget, 2, 0, 1, 2)
        self.setLayout(layout)

        self.solve_widget.clear_button.clicked.connect(
            self.mpl_viewer.clear)
        self.solve_widget.reset_button.clicked.connect(
            self.reset)

        ## Bounds Widget and Path Viewer MPL.
        ## Connections are very loopy atm
        self.bounds_widget.reset_button.clicked.connect(
            self.mpl_viewer.reset_bounds)
        self.bounds_widget.bounds_low.value_changed.connect(
            self.mpl_viewer.set_lower_bounds)
        self.bounds_widget.bounds_high.value_changed.connect(
            self.mpl_viewer.set_upper_bounds)

    def reset(self):
        self.problem_widget.reset()
        self.planners_widget.reset()
        self.bounds_widget.reset()

    def get_bounds(self):
        return self.bounds_widget.get_bounds()

    def get_selected_planners(self):
        return self.planners_widget.get_selected_planners()
    
    def get_propagation(self):
        return self.planners_widget.get_propagation()
    
    def get_min_control_duration(self):
        return self.planners_widget.get_min_control_duration()
    
    def get_max_control_duration(self):
        return self.planners_widget.get_max_control_duration()
    
    def get_planner_options(self):
        return self.planners_widget.get_planner_options()
    
    def get_time_limit(self):
        return self.planners_widget.get_time_limit()

    def enable_plot_button(self, set_enabled=True):
        return self.solve_widget.enable_plot_button(set_enabled=set_enabled)
    
    def enable_plans_button(self, set_enabled=True):
        return self.solve_widget.enable_plans_button(set_enabled=set_enabled)
    
    def get_start_pose(self):
        return self.problem_widget.get_start_pose()

    def get_goal_pose(self):
        return self.problem_widget.get_goal_pose()

    def get_robot_type(self):
        return self.problem_widget.get_robot_type()
