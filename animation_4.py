import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N = 50
growth = 60
blit = True
colored = True

if colored:
    facecolor,lw = '#FFFFFF',3.0
else:
    facecolor,lw = None,0.5

fig = plt.figure(figsize=(7,7),facecolor=facecolor)
ax = plt.axes([0,0,1,1],xlim=(0,1),ylim=(0,1),frameon=False)
ax.set_xticks([])
ax.set_yticks([])

rain = np.zeros(N,dtype=[('center',float,2),('radius',float,1),('growth',float,1),('color',float,4)])

if colored:
    rain['color'][:,:3] = np.random.uniform(0,1,(N,3))
    rain['color'][:,3] = 1
else:
    rain['color'][:,:] = np.asarray([0,0,1,1])

rain['center'][:,:2] = np.random.uniform(0,1,(N,2))
rain['growth'][:] = np.random.uniform(50,200,N)

scat = ax.scatter(rain['center'][:,0],rain['center'][:,1],s=rain['radius'],\
                    lw=lw,edgecolors=rain['color'],facecolors='none')

def init():
    return scat,

def animate(F):
    index = F%N

    rain['color'][:,3] -= 1/N
    rain['color'][:,3] = np.clip(rain['color'][:,3],0,1)
    rain['radius'] += rain['growth']

    rain['center'][index] = np.random.uniform(0,1,2)
    rain['radius'][index] = 0
    if colored:
        rain['color'][index,:3] = np.random.uniform(0,1,3)
        rain['color'][index,3] = 1
    else:
        rain['color'][index,3] = 1
            

    scat.set_edgecolors(rain['color'])
    scat.set_sizes(rain['radius'])
    scat.set_offsets(rain['center'])
    return scat,

if blit:
    anim = animation.FuncAnimation(fig,animate,init_func=init,interval=10,blit=True)
else:
    anim = animation.FuncAnimation(fig,animate,init_func=init,interval=10,blit=False)

plt.show()
