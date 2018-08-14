import sys
sys.path.append('F:/')
import support
print(support.absolute_diff(-9,4))
#-----------------------------------------------------------------------#
import math
import matplotlib.pyplot as plt

write = True
X = []
Y = []


file = open("foo.txt","r+")

if write:
    for i in range(1,361):
        X.append(i)
        Y.append(math.sin(math.radians(i)))
    for i in range(0,360):
        file.write(str(X[i]) + '\t' + str(Y[i]) + '\n')

else:
    _X = []
    _Y = []
    file.seek(0,0)
    for line in file:
        point = line.split("\t")
        _X.append(float(point[0]))
        _Y.append(float(point[1]))
    plt.plot(_X,_Y)
    plt.xlim(min(_X)-1,max(_X)+1)
    plt.ylim(min(_Y)-1,max(_Y)+1)
    plt.show()

