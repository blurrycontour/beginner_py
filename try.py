import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes([0,0,1,1],xlim=(-4,4),ylim=(-4,4),frameon=False)
ax.set_xticks([])
ax.set_yticks([])
points, = ax.plot([],[],marker='o',lw=2,linestyle='')

file = open('data.txt','r')
X=[]
Y=[]
for line in file:
    coords = line.split(",")
    coords = [float(element) for element in coords]
    X.append(coords[0::2])
    Y.append(coords[1::2])

#print(np.asarray(X,dtype='float'))
#print(np.asarray(Y,dtype='float'))


def init():
    points.set_data([],[])
    return points,

def animate(F):
    points.set_data(X[F],Y[F])
    return points,


anim = animation.FuncAnimation(fig,animate,init_func=init,interval=5,blit=True)
plt.show()