#!/usr/bin/env python
"""
# Title: PlannersWidget
# Description: QWidget for setting Planner information
# Author: @moriarty, @amdshameer
# Licence: 
"""

from PyQt4 import QtGui, QtCore
from ompl import base as ob
from ompl import geometric as og
from ompl import control as oc
from ompl import app as oa

from PlannersBox import PlannersBox

import ompl
from decimal import Decimal
ompl.initializePlannerLists()
"""
class PlannersWidget(QtGui.QStackedWidget):
    #docstring for PlannersWidget
    def __init__(self):
        super(PlannersWidget, self).__init__()
"""        
class PlannerHelperWidget(QtGui.QGroupBox):
    def __init__(self, name, planners):
        super(PlannerHelperWidget, self).__init__(name)
        self.setFlat(True)
        self.plannerSelect = QtGui.QComboBox()
        self.stackedWidget = QtGui.QStackedWidget()

        self.plannerList = []
        for planner, params in sorted(planners.items()):
            displayName = planner.split('.')[-1]
            self.plannerSelect.addItem(displayName)
            options = QtGui.QGroupBox('%s options' % displayName)
            layout = QtGui.QGridLayout()
            i = 0
            paramDict = {}
            for (key,val) in sorted(params.items()):
                label = QtGui.QLabel(val[0])
                if val[1] == ompl.PlanningAlgorithms.BOOL:
                    widget = QtGui.QCheckBox()
                    widget.setChecked(val[3])
                elif val[1] == ompl.PlanningAlgorithms.ENUM:
                    widget = QtGui.QComboBox()
                    widget.addItems(val[2])
                    widget.setCurrentIndex(val[3])
                elif val[1] == ompl.PlanningAlgorithms.INT:
                    widget = QtGui.QSpinBox()
                    widget.setRange(val[2][0], val[2][2])
                    widget.setSingleStep(val[2][1])
                    widget.setValue(val[3])
                elif val[1] == ompl.PlanningAlgorithms.DOUBLE:
                    widget = QtGui.QDoubleSpinBox()
                    numDecimals = max([-Decimal(str(v)).as_tuple().exponent for v in val[2]])
                    if numDecimals < 2:
                        numDecimals = 2
                    elif numDecimals > 5:
                        numDecimals = 5
                    widget.setDecimals(numDecimals)
                    widget.setRange(val[2][0], val[2][2])
                    widget.setSingleStep(val[2][1])
                    widget.setValue(val[3])
                else:
                    print("Warning: parameter of unknown type ignored!")
                    continue
                layout.addWidget(label, i, 0, QtCore.Qt.AlignRight)
                layout.addWidget(widget, i, 1)
                i = i + 1
                paramDict[key] = widget
            options.setLayout(layout)
            self.stackedWidget.addWidget(options)
            self.plannerList.append((planner,paramDict))

        self.plannerSelect.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.plannerSelect.currentIndexChanged[int].connect(self.stackedWidget.setCurrentIndex)

class ControlPlannerWidget(PlannerHelperWidget):
    def __init__(self):
        super(ControlPlannerWidget, self).__init__('Planning with controls', oc.planners.getPlanners())

        # make KPIECE1 the default planner
        self.plannerSelect.setCurrentIndex([p[0] for p in self.plannerList].index('ompl.control.KPIECE1'))

        timeLimitLabel = QtGui.QLabel('Time (sec.)')
        self.timeLimit = QtGui.QDoubleSpinBox()
        self.timeLimit.setRange(0, 1000)
        self.timeLimit.setSingleStep(1)
        self.timeLimit.setValue(10.0)

        propagationLabel = QtGui.QLabel('Propagation\nstep size')
        propagationLabel.setAlignment(QtCore.Qt.AlignRight)
        self.propagation = QtGui.QDoubleSpinBox()
        self.propagation.setRange(0.01, 1000.00)
        self.propagation.setSingleStep(.01)
        self.propagation.setValue(0.2)
        self.propagation.setDecimals(2)

        durationLabel = QtGui.QLabel('Control duration\n(min/max #steps)')
        durationLabel.setAlignment(QtCore.Qt.AlignRight)
        self.minControlDuration = QtGui.QSpinBox()
        self.minControlDuration.setRange(1, 1000)
        self.minControlDuration.setSingleStep(1)
        self.minControlDuration.setValue(1)
        self.maxControlDuration = QtGui.QSpinBox()
        self.maxControlDuration.setRange(1, 1000)
        self.maxControlDuration.setSingleStep(1)
        self.maxControlDuration.setValue(20)

        layout = QtGui.QGridLayout()
        layout.addWidget(QtGui.QLabel('Planner'), 0, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.plannerSelect, 0, 1, 1, 2)
        layout.addWidget(timeLimitLabel, 1, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.timeLimit, 1, 1, 1, 2)
        layout.addWidget(propagationLabel, 2, 0, QtCore.Qt.AlignRight)
        layout.addWidget(self.propagation, 2, 1, 1, 2)
        layout.addWidget(durationLabel, 3, 0)
        layout.addWidget(self.minControlDuration, 3, 1)
        layout.addWidget(self.maxControlDuration, 3, 2)
        layout.addWidget(self.stackedWidget, 4, 0, 1, 3)
        self.setLayout(layout)

class PlannersWidget(QtGui.QWidget):
    def __init__(self):
        super(PlannersWidget, self).__init__()
        self.plannersBox = PlannersBox("Pick Planners")
        self.controlPlanning = ControlPlannerWidget()

        layout = QtGui.QGridLayout()
        layout.addWidget(self.plannersBox,0,0)
        layout.addWidget(self.controlPlanning,1,0)
        self.setLayout(layout)
       
