# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 09:24:23 2020

@author: Dell
"""
import numpy as np


def point_source(x: float, y: float, z: float, S:float, sigma: float):
    """
    

    Parameters
    ----------
    x : float
        DESCRIPTION.
    y : float
        DESCRIPTION.
    z : float
        DESCRIPTION.
    S : float
        DESCRIPTION.
    sigma : float
        DESCRIPTION.

    Returns
    -------
    None.

    """
    top = -sigma * S
    bottom = 4*np.pi*np.sqrt(x**2 + y**2 + z**2)
    return top/bottom

def doublet(x: float, y: float, z: float, S: float, mu: float):
    """
    

    Parameters
    ----------
    x : float
        DESCRIPTION.
    y : float
        DESCRIPTION.
    z : float
        DESCRIPTION.
    S : float
        DESCRIPTION.
    mu : float
        DESCRIPTION.

    Returns
    -------
    None.

    """
    first = (-mu*S)/(4*np.pi)
    second = z*(x**2 + y**2 + z**2)**(-3/2)
    return first*second



def calc_field(sigma=1, mu=1, size=2):
    line = np.linspace(-size, size, 100)
    x, y = np.meshgrid(line, line)
    