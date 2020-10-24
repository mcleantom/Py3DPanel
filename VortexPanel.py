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
    Initialise a quadrilateral panel between two points in 3D space
    
    Inputs:
        x0,y0,z0 -- The coordinates of point 0
        x1,y1,z1 -- The coordinates of point 1
        x2,y2,z2 -- The coordinates of point 2
        x3,y3,z3 -- The coordinates of point 3
        gamma -- the panel vortex strength
        
    Outputs:
        A panel object.
    """
    
    def __init__(self, x0, x1, x2, x3, y0, y1, y2, y3, z0, z1, z2, z3):
        self.x = (x0, x1, x2, x3)
        self.y = (y0, y1, y2, y3)
        self.z = (z0, z1, z2, z3)
        
        self.cx = sum(self.x)/4
        self.cy = sum(self.y)/4
        self.cz = sum(self.z)/4
        
        self.A = np.array([(x2-x0), (y2-y0), (z2-z0)]).T
        self.B = np.array([(x3-x1), (y3-y1), (z3-z1)]).T
        self.S = np.abs(np.cross(self.A, self.B))/2
    
    def plot(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        verts = [list(zip(self.x, self.y, self.z))]
        ax.add_collection3d(Poly3DCollection(verts))
        plt.show()
        