import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from math import sin,cos

fig = plt.figure()
ax = plt.axes(xlim=(-1,1),ylim=(-1,1),aspect = 'equal')
point, = ax.plot([],[],'bo',lw=2)
line, = ax.plot([],[],lw=2)
th = 0

def init():
    point.set_data([],[])
    line.set_data([],[])
    return point,

def animate(i):
    global th
    l = np.linspace(0,0.5,10)
    th = i*np.pi/100
    point.set_data([0.5*cos(th),0],[0.5*sin(th),0])
    line.set_data(l*np.sin(th),l*np.cos(th))
    return point,


anim = animation.FuncAnimation(fig,animate,init_func=init,frames=20000,interval=20,blit=True)

plt.show()
