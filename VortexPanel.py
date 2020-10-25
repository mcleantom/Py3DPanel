"""
This module holds routines to determine the potential flow
around bodies of any shape or number using vortex panels.

Classes:
    
Methods:
    
Imports:
    
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Panel(object):
    """
    Initialise a quadrilateral panel between four points in 3D space
    
    Inputs:
        x0,y0,z0 -- The coordinates of point 0
        x1,y1,z1 -- The coordinates of point 1
        x2,y2,z2 -- The coordinates of point 2
        x3,y3,z3 -- The coordinates of point 3
        gamma -- the panel vortex strength
        
    Outputs:
        A panel object.
    """
    
    def __init__(self, x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4):
        """
        """
        self.x = (x1, x2, x3, x4) # Quadrilateral x coordinates
        self.y = (y1, y2, y3, y4) # Quadrilateral y coordinates
        self.z = (z1, z2, z3, z4) # Quadrilateral z coordinates
        
        self.cx = sum(self.x)/4 # Panel centre x coordinate
        self.cy = sum(self.y)/4 # Panel centre y coordinate
        self.cz = sum(self.z)/4 # Panel centre z coordinate
        
        self.A = np.array([(x3-x1), (y3-y1), (z3-z1)]).T # Panel diagonal
        self.B = np.array([(x4-x2), (y4-y2), (z4-z2)]).T # Panel diagonal
        self.S = np.abs(np.cross(self.A, self.B))/2 # Perpendicular vector
        
        # Longitudinal unit vector
        ux = (x1+x2-x3-x4)/2
        uy = (y1+y2-y3-y4)/2
        uz = (z1+z2-z3-z4)/2
        
        # Transverse unit vector
        px = (x2+x3-x4-x1)/2
        py = (y2+y3-y4-y1)/2
        pz = (z2+z3-z4-z1)/2
        
        self.gamma = 0 # Panel vortex strength
    
    def plot(self):
        """
        Plot the panel in 3D space
        """

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        verts = [list(zip(self.x, self.y, self.z))]
        ax.add_collection3d(Poly3DCollection(verts))
        plt.show()


class panels(object):
    """
    """
    
    def __init__(self, panels):
        self.panels = panels
    
    def solve_gamma(self):
        """
        """
        A, b = self._construct_A_b()
        
    def _construct_A_b(self):
        """
        """
        
    def get_array(self):
        """
        """


one_panel = Panel(0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0)
pans = panels([one_panel])
