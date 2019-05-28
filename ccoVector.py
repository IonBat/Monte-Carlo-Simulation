#cc0Vectoro.py
#created by Eng'r Celso B. Co, PhD, PECE
#November 8, 2011



import sympy as sm
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import linalg, mat
import matplotlib.pyplot as plt
#mpl.rcParams['legend.fontsize'] = 10

'''cco modification of library
File:C\Python27\Lib\site-pakages\mpl_toolkits\mplot3d\axes3d.py
line no 777
Original Codes
       shade = []
        for n in normals: 
            if g<>0.0:n = n / proj3d.mod(n)
            shade.append(np.dot(n, [-1, -1, 0.5]))
Change
         shade = [];print "normals=",normals
        for n in normals: #modified by celso co
            g=proj3d.mod(n);#print "g = ",g
            if g<>0.0:n = n / proj3d.mod(n);#print "n = ",n  
            shade.append(np.dot(n, [-1, -1, 0.5]))
Reason: To suppress warnings
'''


def Adjust_Latex(s): #adjust sympy LaTex for matplot latex
        tx='$'+sm.latex(s)+' $'
        #adjustment on sympy Latex for compatibility with pyplot
        return tx

def ccoCylindricialToCartesian(phi):
    M=np.matrix([
        [np.cos(phi), -np.sin(phi),   0],
        [np.sin(phi),    np.cos(phi), 0],
        [0,                    0,                 1]],dtype=float)
    return M

def ccoCartesianToCylindrical(x,y):
    phi=np.arctan(y/x)
    M=np.matrix([
        [np.cos(phi),  np.sin(phi),   0],
        [-np.sin(phi),  np.cos(phi),  0],
        [0,                    0,                 1]],dtype=float)
    return M

def ccoSphericalToCartesian(theta,phi):
    M=np.matrix([
        [np.sin(theta)*np.cos(phi),np.cos(theta)*np.cos(phi),-np.sin(phi)],
        [np.sin(theta)*np.sin(phi),  np.cos(theta)*np.sin(phi), np.cos(phi)],
        [np.cos(theta),                   -np.sin(theta),                    0                 ]
        ],dtype=float)
    return M

def ccoCartesianToSpherical(x,y,z):
    phi=np.arctan(y/x);theta=np.arctan(np.sqrt(x**2+y**2)/z)
    M=np.matrix([
        [np.sin(theta)*np.cos(phi),   np.sin(theta)*np.sin(phi),   np.cos(theta)],
        [np.cos(theta)*np.cos(phi),  np.cos(theta)*np.sin(phi),  -np.sin(theta)],
        [-np.sin(phi),                          np.cos(phi),                          0                    ]
        ],dtype=float)
    return M



#Plot Operations

class Vector():
    def __init__(self,ax1,ax2,ax3):
        self.v=mat([ax1,ax2,ax3])
        self.abs=np.sqrt(self.v.item(0)**2+self.v.item(1)**2+self.v.item(2)**2)
        if self.vasbs !=0:
            self.unit=self.v/self.abs
        else: self.unit=mat([0,0,0])
        self.angle=np.arccos(self.unit)
    def System(self,coordinate='Cartesian'):
        if coordinate=='Cartesian':
            i, j, k =symbols("\\bf{i} \\bf{j} \\bf{k}")
            return self.v.item(0)*i+self.v.item(1)*j+self.v.item(2)*k
        elif coordinate=='Cylindrical':
            r, phi, z=symbols("\\bf{r} \\bf{\\phi} \\bf{z}")
            return self.v.item(0)*r+self.v.item(1)*phi+self.v.item(2)*z
        elif coordinate=='Spherical':
            r, phi, theta =symbols("\\bf{r} \\{\\phi}} \\bf{\\theta}")
            return self.v.item(0)*r+self.v.item(1)*phi+self.v.item(2)*theta
        else:
            i, j, k =symbols("\\bf{i} \\bf{j} \\bf{k}")
            return "Not valid arguement, Default at Cartesian"




def ccoPlotPoint(loc,r):    
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = r * np.outer(np.cos(u), np.sin(v))+loc.item(0)
    y = r * np.outer(np.sin(u), np.sin(v))+loc.item(1)
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))+loc.item(2)
    plt.plot_surface(x, y, z,  rstride=4, cstride=4, color='k')

def ccoPlotTwoPointsLine(p1,p2):
    plt.plot([p1.item(0),p2.item(0)],
            [p1.item(1),p2.item(1)],
            [p1.item(2),p2.item(2)],color='k')

def ccoPlotLineSegment(At,Seg):
    plt.plot(
            [At.item(0),At.item(0)+Seg.item(0)],
            [At.item(1),At.item(1)+Seg.item(1)],
            [At.item(2),At.item(2)+Seg.item(2)],color='k')

def ccoPlotVect(At,vect,colour):
    plt.plot(
            [At.item(0),At.item(0)+vect.item(0)],
            [At.item(1),At.item(1)+vect.item(1)],
            [At.item(2),At.item(2)+vect.item(2)],color=colour)

def ccoTextLoc(At,vect):
    x=At.item(0)+vect.item(0)
    y=At.item(1)+vect.item(1)
    z=At.item(2)+vect.item(2)
    return x,y,z

def ccoText(At,vect,text,colour,figure):
    ax = figure.gca(projection='3d')
    ax.text(
            At.item(0)+vect.item(0),
            At.item(1)+vect.item(1),
            At.item(2)+vect.item(2), text, color=colour)

def ccoAxesRange(h,figure):
    #ax.plot([0],[0],[0]);
    ax = figure.gca(projection='3d')
    ax.plot(
        [h,-h,0,0, 0,0,0, 0],
        [0, 0,0,h,-h,0,0, 0],
        [0, 0,0,0, 0,0,h,-h],color='y');
    ax.text(h,0,0,'x');ax.text(-h,0,0,'-x')
    ax.text(0,h,0,'y');ax.text(0,-h,0,'-y')
    ax.text(0,0,h,'z');ax.text(0,0,-h,'-z')
    
def ccoTextVect(At,vect,text,colour):
    ax = fig.gca(projection='3d')
    ax.text(
            At.item(0)+vect.item(0),
            At.item(1)+vect.item(1),
            At.item(2)+vect.item(2), text, color=colour)

def ccoPutConeHead(At,To):
    v1=mat('[0;0;1]')
    v2=mat([To.item(0),To.item(1),To.item(2)]).T
    uv1=ccoUnitVect(v1)
    uv2=ccoUnitVect(v2)
    M=ccoRotation(uv1,uv2)
    #2D plot at 3D xy plain
    a=ccoAbsVect(v2)
    r=.01*a;h=.1*a
    phi = np.linspace(0, 2 * np.pi, 100)
    z =np.linspace(0, h, 100)
    z1=np.ones(100)
    x=r*np.cos(phi)
    y=r*np.sin(phi)
    for k in z:
        e=mat([x*k,y*k,z1*-k])
        f=M*e
        x2=np.array(f[0])[0]+At.item(0)+v2.item(0)
        y2=np.array(f[1])[0]+At.item(1)+v2.item(1)
        z2=np.array(f[2])[0]+At.item(2)+v2.item(2)
        plt.plot(x2,y2,z2,color='b')

def ccoPutCircularTail(At,To):
    v1=mat('[0;0;1]')
    v2=mat([To.item(0),To.item(1),To.item(2)]).T
    uv1=ccoUnitVect(v1)
    uv2=ccoUnitVect(v2)
    M=ccoRotation(uv1,uv2)
    #2D plot at 3D xy plain
    r=.1*ccoAbsVect(v2)
    phi = np.linspace(0, 2 * np.pi, 100)
    z1=np.zeros(100)
    x=r*np.cos(phi)
    y=r*np.sin(phi)
    h=mat([x,y,z1])
    h1=M*h
    x2=np.array(h1[0])[0]+At.item(0)
    y2=np.array(h1[1])[0]+At.item(1)
    z2=np.array(h1[2])[0]+At.item(2)
    plt.plot(x2,y2,z2,color='b')

def ccoCircleLineData(At, To, Radius, Resolution):
    v1=mat('[0;0;1]')
    v2=mat([To.item(0),To.item(1),To.item(2)]).T
    uv1=ccoUnitVect(v1)
    uv2=ccoUnitVect(v2)
    M=ccoRotation(uv1,uv2)
    #2D plot at 3D xy plain
    r=Radius
    phi = np.linspace(0, 2 * np.pi, Resolution)
    z=np.zeros(Resolution)
    x=r*np.cos(phi)
    y=r*np.sin(phi)
    h=mat([x,y,z])
    h1=M*h
    x1=np.array(h1[0])[0]+At.item(0)
    y1=np.array(h1[1])[0]+At.item(1)
    z1=np.array(h1[2])[0]+At.item(2)
    return x1,y1,z1


def ccoConeSurfaceData(At, To, Height, Base, Resolution):
    v1=mat('[0;0;1]')
    v2=mat([To.item(0),To.item(1),To.item(2)]).T
    uv1=ccoUnitVect(v1)
    uv2=ccoUnitVect(v2) 
    M=ccoRotation(uv1,uv2)
    u = np.linspace(0, 2 * np.pi, Resolution)
    z=np.linspace(0,1,Resolution)
    r=Base/2.0
    x=r*np.cos(u);y=r*np.sin(u);xyz=mat([x,y,z])
    xyz1=M*xyz
    x1=xyz1[0];y1=xyz1[1];z1=xyz1[2]
    X=np.outer(x,z);Y=np.outer(y,z)
    Z=np.outer(np.ones(np.size(u)),-z*Height)
    X1=np.zeros([10,10]);Y1=np.zeros([10,10]);
    Z1=np.zeros([10,10])
    for i in range(10):
        for j in range(10):
            TEMP2=M*np.mat([X[i][j],Y[i][j],Z[i][j]]).T
            X1[i][j]=TEMP2.item(0)+At.item(0)
            Y1[i][j]=TEMP2.item(1)+At.item(1)
            Z1[i][j]=TEMP2.item(2)+At.item(2)
    return X1,Y1,Z1


#Vector Operations

def ccoAbsVect(v):
    return np.sqrt(v.item(0)**2.0+v.item(1)**2.0+v.item(2)**2.0)

def ccoUnitVect(v):
    absV=ccoAbsVect(v)
    if absV==0: return v
    else:
        return v/absV
    
def ccoRotateAbout(axis,angle):
    if axis=='z':      #axes are z, y, x
        M=mat([
        [np.cos(angle),  -np.sin(angle), 0],
        [ np.sin(angle),  np.cos(angle), 0],
        [                    0,                       0, 1]])
    elif axis=='y':
        M=mat([
        [np.cos(angle),  0, -np.sin(angle)],
        [                     0,  1,                     0],
        [ np.sin(angle),   0, np.cos(angle)]])
    else:
        M=mat([
        [1,                     0,                     0],
        [0,np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]])
    return M

def ccoDotProd(V1,V2):
    return V1.item(0)*V2.item(0)+V1.item(1)*V2.item(1)+V1.item(2)*V2.item(2)

def ccoCrossProd(V1,V2):
    return mat([
        [V1.item(1)*V2.item(2)-V1.item(2)*V2.item(1) ],
        [-V1.item(0)*V2.item(2)+V1.item(2)*V2.item(0) ],
        [V1.item(0)*V2.item(1)-V1.item(1)*V2.item(0) ]])
        
def ccoChooseAxis(From, To):
    uFV=ccoUnitVect(From)
    uTV=ccoUnitVect(To)
    g=mat([
        [uFV.item(0)**2+uTV.item(0)**2-uFV.item(0)**2*uTV.item(0)**2],
        [uFV.item(1)**2+uTV.item(1)**2-uFV.item(1)**2*uTV.item(1)**2],
        [uFV.item(2)**2+uTV.item(2)**2-uFV.item(2)**2*uTV.item(2)**2]])
    Axis='x';
    if g[1]<g[0]:
        Axis='y'
        if g[2]<g[1]:Axis='z'
    elif g[2]<g[0]:Axis='z'    
    return Axis

def ccoNextAxis(After):
    if After=='x':return 'y'
    elif After=='y':return 'z'
    else: return 'x'

def ccoAngleAbout(axis,From,To):
     if axis=='z': n=2
     elif axis=='y': n=1
     else:n=0
     FV=[From.item(0),From.item(1),From.item(2)]
     TV=[To.item(0),To.item(1),To.item(2)]
     FV[n]=0;FV=np.mat(FV);TV[n]=0;TV=np.mat(TV)
     uFV=ccoUnitVect(FV)
     uTV=ccoUnitVect(TV)
     dot=np.dot(uFV,uTV.T).item(0)
     angledot=np.arccos(dot)
     return angledot, uFV, uTV
    
def ccoRotationAbout(Axis,From,To):
    #print "ccoRotationAbout"
    if Axis=='x':n1=1;n2=2#;print " x axis"
    elif Axis=='y':n1=0;n2=2#;print "y axis"
    else:n1=0;n2=1#;print "z axis"
    uF=ccoUnitVect(np.array([From.item(0),From.item(1),From.item(2)]))
    #print "uF = ",uF
    uT=ccoUnitVect(np.array([To.item(0),To.item(1),To.item(2)]))
    #print "uT = ",uT
    b=np.matrix([uT.item(n1),uT.item(n2)]).T
    A=np.matrix([[uF.item(n1),-uF.item(n2)],[uF.item(n2),uF.item(n1)]])
    if linalg.det(A)!=0:
        h=A.I*b#;print "h=",h.T,h.item(0)**2+h.item(1)**2
        if Axis=='x':
            M=np.matrix([
            [1,0,0],
            [0,h.item(0),-h.item(1)],
            [0,h.item(1), h.item(0)]])
        elif Axis=='y':
            M=np.matrix([
            [h.item(0),0,-h.item(1)],
            [0,1,0],
            [h.item(1),0, h.item(0)]])
        else:
            M=np.matrix([
            [h.item(0),-h.item(1),0],
            [h.item(1), h.item(0),0],
            [0,0,1]])
        return M
    else:return []

def ccoRotation(From,To):
    #print "ccoRotation"
    F=np.matrix([From.item(0),From.item(1),From.item(2)])
    T=np.matrix([To.item(0),To.item(1),To.item(2)])
    Axis1=ccoChooseAxis(From,To)#;print "Axis1 = ",Axis1
    uF=ccoUnitVect(F)#;print "uF = ",uF
    uT=ccoUnitVect(T)#;print "uT = ",uT
    M1=ccoRotationAbout(Axis1,uF,uT)
    uv1=M1*uF.T#;print "uv1=",uv1.T
    Axis2=ccoNextAxis(Axis1)#;print "Axis2 =",Axis2
    M2=ccoRotationAbout(Axis2,uv1,uT)
    if M2!= []:
        uv2=M2*uv1#;print "uv2=",uv2.T
        M=M2*M1
    else:
        Axis3=ccoNextAxis(Axis2)#;print "Axis3 = ",Axis3
        M3=ccoRotationAbout(Axis3,uv1,uT)
        if M3!=[]:M=M3*M1
        else:M=M1
    uv3=M*uF.T#;print "uv3=",uv3.T
    return M                               
