#!/usr/bin/env python
"""
# Title: MyStaticMplCanvas
# Description: Simple Static MatPlotLib Canvas for testing MPL in Qt
# Author: @moriarty, @amdshameer
# Licence: 
"""


from PyQt4 import QtGui

class SolveWidget(QtGui.QWidget):
    """Solve Widget 

    A simple QWidget to hold Solve and Clear buttons
    """
    def __init__(self):
        super(SolveWidget, self).__init__()
        self.solve_button = QtGui.QPushButton('Solve')
        self.plot_button = QtGui.QPushButton('Plot')
        self.clear_paths = QtGui.QPushButton('Clear Plans')
        self.clear_button = QtGui.QPushButton('Clear Plot')
        self.reset_button = QtGui.QPushButton('Reset ALL Settings')

        self.enable_plot_button(False)
        self.enable_plans_button(False)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.solve_button, 0, 0)
        layout.addWidget(self.plot_button, 0, 1)
        layout.addWidget(self.clear_paths, 0, 2)
        layout.addWidget(self.clear_button, 0, 3)
        layout.addWidget(self.reset_button, 0, 4)
        self.setLayout(layout)

    def enable_plot_button(self, set_enabled=True):
        self.plot_button.setEnabled(set_enabled)

    def enable_plans_button(self, set_enabled=True):
        self.clear_paths.setEnabled(set_enabled)

