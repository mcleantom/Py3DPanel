# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:18:54 2020

@author: Rastko
"""

from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation
import pandas as pd
from scipy.spatial.transform import Rotation as R


def differentiate(df, columns, time_column_name="Time"):
    """
    """
    time_step = df[time_column_name][1]-df[time_column_name][0]
    print(time_step)
    return df[columns].diff()/time_step


def scalar_projection(a, b):
    """
    """
    dot_product = np.einsum('ij, ij-> i', a, b)  # np.dot(a, b)
#    print(dot_product)
    scalar = np.linalg.norm(b, axis=1)
#    print(scalar)
    return dot_product/scalar


def compute_segs(i):
    """
    """
    x = [position["X"][i]]*3
    y = [position["Y"][i]]*3
    z = [position["Z"][i]]*3

    u = [position["X"][i]+rotated_x_vector[i][0],
         position["X"][i]+rotated_y_vector[i][0],
         position["X"][i]+rotated_z_vector[i][0]]

    v = [position["Y"][i]+rotated_x_vector[i][1],
         position["Y"][i]+rotated_y_vector[i][1],
         position["Y"][i]+rotated_z_vector[i][1]]

    w = [position["Z"][i]+rotated_x_vector[i][2],
         position["Z"][i]+rotated_y_vector[i][2],
         position["Z"][i]+rotated_z_vector[i][2]]

    return x, y, z, u, v, w


def animate(i):
    """
    """
    segs = np.array(compute_segs(i)).reshape(6, -1)
    new_segs = [[[x, y, z], [u, v, w]] for x, y, z, u, v, w in zip(*segs.tolist())]
    quivers.set_segments(new_segs)
    return quivers


fig = plt.figure()
ax = fig.gca(projection='3d')

num_frames = 12000

df = pd.read_excel('sample data.xlsx')
rotation = df[['Rot z', 'Rot y', 'Rot x']]+[0, 0, 0]
position = df[['X', 'Y', 'Z']]
x_vector = np.array([1, 0, 0])
y_vector = np.array([0, 1, 0])
z_vector = np.array([0, 0, 1])

r = R.from_euler('zxy', rotation, degrees=True)
rotated_x_vector = r.apply(x_vector)
rotated_y_vector = r.apply(y_vector)
rotated_z_vector = r.apply(z_vector)
rotated_ax_vectors = [rotated_x_vector, rotated_y_vector, rotated_z_vector]

# =============================================================================
# 
# =============================================================================

velocity =  differentiate(df, ["X", "Y", "Z"])
velocity["Time"] = df["Time"]
acceleration = differentiate(velocity, ["X", "Y", "Z"])

local_acceleration_x = scalar_projection(acceleration, rotated_x_vector)
local_acceleration_y = scalar_projection(acceleration, rotated_y_vector)
local_acceleration_z = scalar_projection(acceleration, rotated_z_vector)

# =============================================================================
# 
# =============================================================================
local_x = scalar_projection(position, rotated_x_vector)
local_y = scalar_projection(position, rotated_y_vector)
local_z = scalar_projection(position, rotated_z_vector)

local_x_rot = scalar_projection(rotation, rotated_x_vector)
local_y_rot = scalar_projection(rotation, rotated_y_vector)
local_z_rot = scalar_projection(rotation, rotated_z_vector)

local_position = pd.DataFrame()
local_position["Time"] = df["Time"]
local_position["X"] = local_x
local_position["Y"] = local_y
local_position["Z"] = local_z

position_column_names = list(local_position.columns[1:])
velocity_column_names = [s + '.' for s in position_column_names]
acceleration_column_names = [s + '.' for s in velocity_column_names]

local_position[velocity_column_names] = differentiate(local_position, position_column_names)
local_position[acceleration_column_names] = differentiate(local_position, velocity_column_names)

local_position["Acc. mag"] = np.linalg.norm(local_position[["X..", "Y..", "Z.."]], axis=1)

segs = compute_segs(0)
cols = ['r', 'k', 'k']
quivers = ax.quiver(*segs, length=1, normalize=True, colors=cols)

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])


ax.set_xlim3d([-2.0, 2.0])
ax.set_xlabel('X')

ax.set_ylim3d([-2.0, 2.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-2, 2])
ax.set_zlabel('Z')
ani = FuncAnimation(fig, animate, frames=num_frames, interval=10, blit=False)

plt.show()
