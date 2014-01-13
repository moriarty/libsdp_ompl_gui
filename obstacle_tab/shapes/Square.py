#!/usr/bin/env python
"""
# Title: Square
# Description: A square obstacle
# Author: @moriarty, @amdshameer
# Licence:
"""
# import statement
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal as Signal

# Square class
class Square(QtGui.QGroupBox):
    """
    Simple Square obstacle
    """
    size_changed = Signal(list)

    def __init__(self, title):
        super(Square, self).__init__(title)
        size_label = QtGui.QLabel('Square Size')
        
        self.size = QtGui.QDoubleSpinBox()
        self.size.setRange(1, 10)
        self.size.setSingleStep(0.5)

        layout = QtGui.QGridLayout()
        layout.addWidget(size_label, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.size, 1, 1, QtCore.Qt.AlignLeft)
        self.setLayout(layout)

        ## Connect a change in size to sizeChange()
        self.size.valueChanged.connect(self.size_change)

    def get_size(self):
        """ returns bounds: [ size ] """
        return [self.size.value()]

    def size_change(self):
        """Emits size_shanged Signal [ size]"""
        self.size_changed.emit(self.get_size())

    def get_info(self):
        info = {}
        info.update({"size": self.get_size()[0]})
        return info

