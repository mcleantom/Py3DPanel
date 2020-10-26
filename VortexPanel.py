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
    
    def __init__(self, points, gamma=1):
        """
        
        """
        self.points = points # Copy of points, make it a np array
        
        self.x = points[:,0] # Quadrilateral x coordinates
        self.y = points[:,1] # Quadrilateral y coordinates
        self.z = points[:,2] # Quadrilateral z coordinates
        
        self.cx = sum(self.x)/4 # Panel centre x coordinate
        self.cy = sum(self.y)/4 # Panel centre y coordinate
        self.cz = sum(self.z)/4 # Panel centre z coordinate
        
        self.A = np.array([(self.x[2]-self.x[0]),
                           (self.y[2]-self.y[0]),
                           (self.z[2]-self.z[0])]).T # Panel diagonal
        
        self.B = np.array([(self.x[3]-self.x[1]),
                           (self.y[3]-self.y[1]),
                           (self.z[3]-self.z[1])]).T # Panel diagonal
        
        self.n = np.abs(np.cross(self.A, self.B))/2 # Normal vector
        
        # # Longitudinal unit vector
        self.ux = -(self.x[0]+self.x[1]-self.x[2]-self.x[3])/2
        self.uy = -(self.y[0]+self.y[1]-self.y[2]-self.y[3])/2
        self.uz = -(self.z[0]+self.z[1]-self.z[2]-self.z[3])/2
        self.u = np.array([self.ux, self.uy, self.uz])
        
        # # Transverse unit vector
        self.px = (self.x[1]+self.x[2]-self.x[3]-self.x[0])/2
        self.py = (self.y[1]+self.y[2]-self.y[3]-self.y[0])/2
        self.pz = (self.z[1]+self.z[2]-self.z[3]-self.z[0])/2
        self.p = np.array([self.px, self.py, self.pz])
        
        self.o = np.cross(self.n, self.u) 
        
        self.S = np.abs(np.cross(self.A, self.B))/2
        
        self.gamma = gamma
        self.sigma = self.calc_sigma()
    
    def plot(self):
        """
        Plot the panel in 3D space
        """

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        verts = [list(zip(self.x, self.y, self.z))]
        ax.add_collection3d(Poly3DCollection(verts))
        plt.show()
    
    def calc_sigma(self, U=np.array([1,0,0])):
        """
        Calculates the source strength, sigma.
        """
        sigma = np.dot(self.n, U)
        return sigma

    def transform_to_local(self, global_coords):
        """
        
        """
        transform_matrix = np.array([self.u,
                                     self.o,
                                     np.zeros(3)])#
        print(transform_matrix)
        return np.matmul(transform_matrix,global_coords)
    
    def transform_to_global(self, local_coordinates):
        """
        
        """
        

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
        Construct the linear system to enforce no-slip on every panel
        
        Outputs:
        A - dipole influence coefficient matrix
        b - source influence coefficient patrix
        """
        xc,yc,zc,sx,sy,sz = self.get_array('xc','yc','zc','sx','sy','sz')
        
    def get_array(self, key, *args):
        """
        """
        if not args:
            return np.array([getattr(p,key) for p in self.panels])
        else:
            return [self.get_array(k) for k in (key,)+args]

corners = np.array([[0,0,1],
                    [1,0,1],
                    [1,0.5,1],
                    [0,0.5,1]])
one_panel = Panel(corners)
one_panel.plot()
pans = panels([one_panel])
