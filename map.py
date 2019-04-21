#%%
from matplotlib import pyplot as plt
import numpy as np 


def plot_map(nrow, ncol, obstacles):
    fig = plt.figure()
    ax  = fig.gca()
    ax.grid(True)
    ax.axis([0,ncol,0,nrow])
    ax.set_aspect('equal')
    for i in obstacles:
        rect = plt.Rectangle(i,1,1)
        ax.add_patch(rect)
    return fig, ax
