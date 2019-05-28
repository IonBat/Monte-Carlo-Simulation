# -*- coding: utf-8 -*-
#Cartesian Coordinate System
#File Name: 1.3 Figure.py
#Created by Eng'r Celso Bation Co, PhD, PECE
#16-Jun-2014


#Library
from ccoPlot import *

def Plt2D(f,t,i,v):
    figure(num=f)
    subplots_adjust(hspace=1)
    subplot(1,3,1)
    ax=gca()
    ax.set_title("Current")
    ax.set_ylabel("mille amp")
    ax.set_xlabel("mille sec")
    ax.plot(t,i)

    subplot(1,3,2)
    ax=gca()
    ax.set_title("voltage")
    ax.set_ylabel("volt")
    ax.set_xlabel("mille sec")
    ax.plot(t,v)

    subplot(1,3,3)
    ax=gca()
    ax.set_title("VI Curve")
    ax.set_ylabel("mille amp")
    ax.set_xlabel("volt")
    ax.plot(i,v)


def Plt3D(f,t,i,v):
    ax=Axes3D(figure(num=f))
    subplots_adjust(hspace=1)
    ax.set_title("Voltage, Current, Time")
    ax.set_ylabel("volt")
    ax.set_xlabel("mille sec")
    ax.set_zlabel("mille amp")
    ax.plot3D(t,v,i)
