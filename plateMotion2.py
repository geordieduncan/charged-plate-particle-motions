import math
import matplotlib.pyplot as plot
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
    for i in range(1000):
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
    plot.plot(X,Z,'ro')
print "type plateMotion(x-start,y-start,z-start,delta,coeffecient of accuracy,and time step)"
print "the coordinates represent distances from the center of a 1x1 square on the xy plane, delta represents the charge of unbalanced charges per square meter on the plate (given that it is a 1x1 plate this is just the charge value of the plate,  coeffecient of accuracy is determines how close to an integration this summation is, the closer to infinite, the slower the program will run, but the more accurate the data will be, the program executes 100 coordinate calculations, the last input determines the number of seconds between calculations, this value needs to be tweaked depending on other inputs for useful results, accurate results are typically no more than 5 cm different each calculation for the first 10 at least"
plateMotion(-0.5,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.45,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.4,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.35,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.3,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.25,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.2,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.15,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.1,0.0,0.001,5e-6,20,5e-12)
plateMotion(-0.05,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.0,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.1,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.5,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.45,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.4,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.35,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.3,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.25,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.2,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.15,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.1,0.0,0.001,5e-6,20,5e-12)
plateMotion(0.05,0.0,0.001,5e-6,20,5e-12)

plot.show()
