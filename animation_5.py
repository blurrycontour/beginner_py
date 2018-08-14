import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import animation

COLOR = 'r'
TYPE = 1
LENGTH = 500

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],111,projection='3d')

ax.set_xlim3d([-1.0,1.0])
ax.set_xlabel('X')
ax.set_ylim3d([-1.0,1.0])
ax.set_ylabel('Y')
ax.set_zlim3d([-1.0,1.0])
ax.set_zlabel('Z')
ax.set_title('3D Lines')

def get_data(length=50,step=0.1):
    dat = np.empty([length,3])
    dat[0] = np.zeros(3)
    for i in range(1,length):
        dat[i] = dat[i-1] + (step*np.random.uniform(-1,1,3))

    return dat

def update(F):
    line.set_data(data[:F,0],data[:F,1])
    line.set_3d_properties(data[:F,2])
    #line = ax.plot(data[:F,0],data[:F,1],data[:F,2])[0]
    return line,

if TYPE is 1:
    data = [0.7*np.random.uniform(-1,1,3) for i in range(LENGTH)]
    data = np.asarray(data,dtype='float')  
    print(data) 
else:
    data = get_data(LENGTH,0.1)
    print(data)
    

line = ax.plot([0.0],[0.0],[0.0],color=COLOR)[0]
#ax.plot(data[:,0],data[:,1],data[:,2])

anim = animation.FuncAnimation(fig,update,frames=LENGTH,interval=50,blit=False)
plt.show()