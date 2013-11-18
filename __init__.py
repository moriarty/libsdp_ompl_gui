"""
ompl_gui package

A package containing classes related to a simple Open Motion Planning Library GUI
"""
__all__=['BoundsBox.py', 'MplCanvas', 'MyStaticMplCanvas', 
         'Pose2DBox.py', 'SolveWidget', 'BoundsWidget', 
         'MainWidget', 'MPLViewer', 'PlannersWidget', 
         'ProblemWidget']

#from bounds_tab import BoundsBox
#from MplCanvas import MplCanvas
#from MyStaticMplCanvas import MyStaticMplCanvas
from Pose2DBox import Pose2DBox
from SolveWidget import SolveWidget
from bounds_tab import BoundsWidget
from MainWidget import MainWidget
from plot_view import MPLViewer
from PlannersWidget import PlannersWidget
from problem_tab import ProblemWidget
