import math
from random import random as rand
from math import pi as pi
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X=[]
Y=[]
Z=[]
T=[]
def plateMotion(x,y,z,delta,n,tstep):
    n=float(n)
    delta=float(delta)
    x=float(x)
    y=float(y)
    z=float(z)
    tstep=float(tstep)
    xv=0
    yv=0
    zv=0
    t=0
    for i in range(200):
        xforce=0
        yforce=0
        zforce=0
        for a in range(int(-n/2),int((n)/2)+1):
            for b in range(int(-n/2),int((n)/2)+1):
                d=math.sqrt((x-(a/n))**2+(y-(b/n))**2+z**2)
                xforce+= (((x-(a/n)))/d)*(delta)*(1.4418e-9/(d*n)**2)
                yforce+= (((y-(b/n)))/d)*(delta)*(1.4418e-9/(d*n)**2)
                zforce+= (z/d)*(delta)*(1.4418e-9/(d*n)**2)
        xac = 1820*xforce/(1.67*10**-27)
        xv+= xac*tstep
        x+=xv*tstep
        yac = 1820*yforce/(1.67*10**-27)
        yv+= yac*tstep
        y+=yv*tstep
        zac = 1820*zforce/(1.67*10**-27)
        zv+= zac*tstep
        z+=zv*tstep
        X.append(x)
        Y.append(y)
        Z.append(z)
        t+=tstep
        T.append(t)
    """
    print 'x-values:'
    print X
    print 'y-values:'
    print Y
    print 'z-values'
    print Z
    print 'times:'
    print T
    """
def rotMot(r):
    x=rand()
    plateMotion(r*math.cos(0+x),0.25*math.sin(0+x),0.05,5e-6,20,25e-12)
    x=rand()
    plateMotion(r*math.cos((pi/4)+x),r*math.sin((pi/4)+x),0.05,5e-6,20,25e-12)
    x=rand()
    plateMotion(r*math.cos((pi/2)+x),r*math.sin((pi/2)+x),0.05,5e-6,20,25e-12)
    x=rand()
    plateMotion(r*math.cos((3*pi/4)+x),r*math.sin((3*pi/4)+x),0.05,5e-6,20,25e-12)
    x=rand()
    plateMotion(r*math.cos((pi)+x),r*math.sin((pi)+x),0.05,5e-6,20,25e-12)
    x=rand()
    plateMotion(r*math.cos((5*pi/4)+x),r*math.sin((5*pi/4)+x),0.05,5e-6,20,25e-12)
    x=rand()
    plateMotion(r*math.cos((3*pi/2)+x),r*math.sin((3*pi/2)+x),0.05,5e-6,20,25e-12)
    x=rand()
    plateMotion(r*math.cos((7*pi/4)+x),r*math.sin((7*pi/4)+x),0.05,5e-6,20,25e-12)
def flower():
    rotMot(.1)
    rotMot(.2)
    rotMot(.3)
    rotMot(.4)
    rotMot(.5)
    plateMotion(0.0,0.0,0.05,5e-6,20,25e-12)
    ax.scatter(np.array(X),np.array(Y),np.array(Z))
    plt.show()
def single(x,y,z,delta,n,tstep):
    plateMotion(x,y,z,delta,n,tstep)
    ax.scatter(np.array(X),np.array(Y),np.array(Z))
    plt.show()
flower()