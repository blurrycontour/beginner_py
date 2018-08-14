import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from math import pow,atan,sin,cos

K = -1000000
T = 0.01
MASS = 5
B = 3000
BOUND = [-B,B,-B,B]
V_MAX = 100
INV = False
EXTRA = False

fig = plt.figure(figsize=(7,7))

if INV:
    ax = plt.axes([0,0,1,1],xlim=(BOUND[0],BOUND[1]),ylim=(BOUND[2],BOUND[3]),axisbg='#000000',frameon=False)
    point, = ax.plot([],[],'wo',lw=2,ms=13)
else:
    ax = plt.axes([0,0,1,1],xlim=(BOUND[0],BOUND[1]),ylim=(BOUND[2],BOUND[3]),axisbg='#000000',frameon=False)
    ax.set_xticks([])
    ax.set_yticks([])
    point, = ax.plot([],[],lw=1,marker='o',linestyle='',aa=True,label='Points',ms=13)
    #point.set_antialiased(False)
    #point.setp()
if EXTRA:
    plt.xlabel('X', fontsize=14, color='red')
    plt.ylabel('Y', fontsize=14, color='red')
    plt.title('Body Simulation')
    plt.grid(True)
    plt.text(0, 0, r'$\mu=100,\ \sigma=15$')
    plt.legend()
    

class Particle:
    def __init__(self,name,mass,x0,y0,vx0,vy0):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.vx = vx0
        self.vy = vy0
        self.fx = 0
        self.fy = 0
        if mass != 0:
            self.mass = abs(mass)
        else:
            self.mass = 0.0001

def boundary_check():
    for i in range(0,len(p)):
        if(p[i].x < BOUND[0]):
            p[i].vx = -p[i].vx
            p[i].x = BOUND[0]
        if(p[i].x > BOUND[1]):
            p[i].vx = -p[i].vx
            p[i].x = BOUND[1]
        if(p[i].y < BOUND[2]):
            p[i].vy = -p[i].vy
            p[i].y = BOUND[2]
        if(p[i].y > BOUND[3]):
            p[i].vy = -p[i].vy
            p[i].y = BOUND[3]

def velocity_check():
    for i in range(0,len(p)):
        if p[i].vx > V_MAX:
            p[i].vx = V_MAX
        elif p[i].vx < -V_MAX:
            p[i].vx = -V_MAX
        if p[i].vy > V_MAX:
            p[i].vy = V_MAX
        elif p[i].vy < -V_MAX:
            p[i].vy = -V_MAX

def init():
    point.set_data([],[])
    boundary_check()
    velocity_check()
    return point,

def animate(F):
    #print('__________')
    #print(F)
    for i in range(0,len(p)):
        p[i].fx = 0.0
        p[i].fy = 0.0
    for i in range(0,len(p)):
        for j in range(0,len(p)):
            if j > i:
                x = p[i].x-p[j].x
                y = p[i].y-p[j].y
                r = pow(x,2) + pow(y,2)
                f = K*(p[i].mass*p[j].mass)/r
                
                if x != 0:
                    th = atan(abs(y/x))
                elif y != 0:
                    th = np.pi/2
                else:
                    th = th
                
                Fx = f*cos(th)
                Fy = f*sin(th)
                
                if x > 0:
                    p[i].fx += -Fx
                    p[j].fx += Fx
                else:
                    p[i].fx += Fx
                    p[j].fx += -Fx

                if y > 0:
                    p[i].fy += -Fy
                    p[j].fy += Fy
                else:
                    p[i].fy += Fy
                    p[j].fy += -Fy
        
        for i in range(0,len(p)):
            for j in range(0,len(p)):
                if j > i:
                    #p[i].x = p[i].x + 0.5*p[i].fx*T*T/p[i].mass
                    #p[i].y = p[i].y + 0.5*p[i].fy*T*T/p[i].mass
                    #p[j].x = p[j].x + 0.5*p[j].fx*T*T/p[j].mass
                    #p[j].y = p[j].y + 0.5*p[j].fy*T*T/p[j].mass

                    p[i].vx = p[i].vx + T*(p[i].fx/p[i].mass) 
                    p[i].vy = p[i].vy + T*(p[i].fy/p[i].mass)   
                    p[j].vx = p[j].vx + T*(p[j].fx/p[j].mass)
                    p[j].vy = p[j].vy + T*(p[j].fy/p[j].mass)  

                    p[i].x = p[i].x + T*p[i].vx
                    p[i].y = p[i].y + T*p[i].vy
                    p[j].x = p[j].x + T*p[j].vx
                    p[j].y = p[j].y + T*p[j].vy

    
    coordX = []
    coordY = []
    boundary_check()
    velocity_check()
    for i in range(0,len(p)):
        coordX.append(p[i].x)
        coordY.append(p[i].y)
    
    point.set_data(coordX,coordY)
    
    return point,

def save_anim():
    plt.rcParams['animation.ffmpeg_path'] = 'C:\\FFMPEG\\bin\\ffmpeg.exe'
    FFwriter = animation.FFMpegWriter()
    anim.save('basic_animation.mp4', writer = FFwriter, fps=30) 

#_______________________________________________________________________________#

p = []
p1 = Particle('1',MASS,-250,0,0,0)
p2 = Particle('2',MASS,-250,250,0,0)
p3 = Particle('3',MASS,0,250,0,0)
p4 = Particle('4',MASS,250,250,0,0)
p5 = Particle('5',MASS,250,0,0,0)
p6 = Particle('6',MASS,250,-250,0,0)
p7 = Particle('7',MASS,0,-250,0,0)
p8 = Particle('8',MASS,-250,-250,0,0)
p.append(p1)
p.append(p2)
p.append(p3)
p.append(p4)
p.append(p5)
p.append(p6)
p.append(p7)
p.append(p8)


anim = animation.FuncAnimation(fig,animate,init_func=init,frames=10000,interval=20,blit=True)
#save_anim()
plt.show()
print(id(p1),id(p[0]))

