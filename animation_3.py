import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation,transforms
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt

RADIUS = 0.04
N = 50
B = 2
BOUND = [-B,B,-B,B]
BORDER = [-(B+RADIUS),B+RADIUS,-(B+RADIUS),B+RADIUS]
dt = 0.01
DPI = 100

fig = plt.figure(figsize=(6,6), dpi=DPI)
ax = plt.axes([0, 0, 1, 1],xlim=(BORDER[0],BORDER[1]),ylim=(BORDER[2],BORDER[3]),\
                axisbg='#FFFFFF',frameon=False)
ax.set_xticks([])
ax.set_yticks([])

points, = ax.plot([],[],'ro',ms=10,aa=True)

ms = int(0.7*fig.get_figwidth()*DPI*2*RADIUS/5.0)
points.set_markersize(ms)

class Particles:
    def __init__(self,mass=1.0,a=[0,-10],r=RADIUS,init_state=[[-1,-1,0,0],[-1,1,0,0],[-1,2,0,0]]):
        "Initialization Function"
        self.m = mass
        self.a = np.asarray(a,dtype='float')
        self.r = r
        self.state = np.asarray(init_state,dtype='float')
        self.I = self.state.shape[0]
        self.J = self.state.shape[1]
        self.col_indices = []
    
    def boundary_check(self):
        "Causes bouncing off the boundary"
        for i in range(0,self.I):
            x = self.state[i,0]
            y = self.state[i,1]
            if x < BOUND[0]:
                self.state[i,0] = BOUND[0]
                self.state[i,2] = -self.state[i,2]
            if x > BOUND[1]:
                self.state[i,0] = BOUND[1]
                self.state[i,2] = -self.state[i,2]
            if y < BOUND[2]:
                self.state[i,1] = BOUND[2]
                self.state[i,3] = -self.state[i,3]
            if y > BOUND[3]:
                self.state[i,1] = BOUND[3]
                self.state[i,3] = -self.state[i,3]

    def step(self):
        "Computes the step" 
        self.state[:,:2] += dt*self.state[:,2:]
        self.boundary_check()

        self.col_indices = []

        for i in range(0,self.I):
            for j in range(0,self.I):
                if j > i:
                    d = sqrt((self.state[i,0]-self.state[j,0])**2 + (self.state[i,1]-self.state[j,1])**2)
                    if d <= 2*self.r:
                          self.col_indices.append([i,j])

        if len(self.col_indices) > 0: 
            for k in range(0,len(self.col_indices)):
                m1 = self.m
                m2 = self.m
                v1 = self.state[self.col_indices[k][0],2:]
                v2 = self.state[self.col_indices[k][1],2:]
                r1 = self.state[self.col_indices[k][0],:2]
                r2 = self.state[self.col_indices[k][1],:2]
                v_rel = v1-v2
                r_rel = r1-r2
                v_dot_r = np.dot(v_rel,r_rel)
                r_dot_r = np.dot(r_rel,r_rel)
                if r_dot_r == 0:
                    continue
                a =  (v_dot_r/r_dot_r)
                v1 += - (2*m2/(m1+m2))*a*r_rel
                v2 += + (2*m1/(m1+m2))*a*r_rel

                self.state[self.col_indices[k][0],2:] = v1
                self.state[self.col_indices[k][1],2:] = v2
        
        self.state[:,2:] += dt*self.a


init_state = np.random.random((N,4))
init_state[:,0] = BOUND[0] + (BOUND[1]-BOUND[0])*init_state[:,0]
init_state[:,1] = BOUND[2] + (BOUND[3]-BOUND[2])*init_state[:,1]
init_state[:,2:] = 3*(-1 + 2*init_state[:,2:])
particles = Particles(init_state=init_state)

def init():
    points.set_data([],[])
    return points,

def animate(F):
    particles.step()    
    points.set_data(particles.state[:,0],particles.state[:,1])
    return points,


anim = animation.FuncAnimation(fig,animate,init_func=init,frames=10000,interval=20,blit=True)
plt.show()
