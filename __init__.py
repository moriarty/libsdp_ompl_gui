"""
ompl_gui package

A package containing classes related to a simple Open Motion Planning Library GUI
"""
__all__=['BoundsBox.py', 'MplCanvas', 'MyStaticMplCanvas', 
         'Pose2DBox.py', 'SolveWidget', 'BoundsWidget', 
         'MainWidget', 'MPLViewer', 'PlannersWidget', 
         'ProblemWidget']

from BoundsBox import BoundsBox
from MplCanvas import MplCanvas
from MyStaticMplCanvas import MyStaticMplCanvas
from Pose2DBox import Pose2DBox
from SolveWidget import SolveWidget
from BoundsWidget import BoundsWidget
# TODO from MainWidget import MainWidget
from MPLViewer import MPLViewer
# TODO from PlannersWidget import PlannersWidget
from ProblemWidget import ProblemWidget
