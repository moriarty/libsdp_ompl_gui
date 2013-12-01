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
        self.solveButton = QtGui.QPushButton('Solve')
        self.plotButton = QtGui.QPushButton('Plot')
        self.clearPaths = QtGui.QPushButton('Clear Plans')
        self.clearButton = QtGui.QPushButton('Clear Plot')
        self.resetButton = QtGui.QPushButton('Reset Settings')

        self.enablePlotButton(False)
        self.enablePlansButton(False)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.solveButton, 0, 0)
        layout.addWidget(self.plotButton, 0, 1)
        layout.addWidget(self.clearPaths, 0, 2)
        layout.addWidget(self.clearButton, 0, 3)
        layout.addWidget(self.resetButton, 0, 4)
        self.setLayout(layout)

    def enablePlotButton(self, setEnabled=True):
        self.plotButton.setEnabled(setEnabled)

    def enablePlansButton(self, setEnabled=True):
        self.clearPaths.setEnabled(setEnabled)

