rom shutil import get_archive_formats
from socket import gaierror
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
class output: 
    @staticmethod
    def every_value(tirray,aarray,verray,herray):
        plt.plot(tirray,verray, label='velocity')
        plt.plot(tirray,herray, label='height')
        plt.plot(tirray, aarray, label='acelleration')
        plt.xlabel('total time')
        plt.ylabel('value')
        plt.title('dependence by time')
        plt.legend()
        plt.show()
    @staticmethod
    def trace (derray,herray):
        plt.plot(derray,herray)
        plt.ylabel('height')
        plt.xlabel('distance')
        plt.title('trace')
        plt.show()
    @staticmethod
    def acelleration (tirray, aarray):
        plt.plot(tirray, aarray)
        plt.ylabel('acelleration')
        plt.xlabel('total time')
        plt.title('acelleration by time')
        plt.show()
    @staticmethod
    def velocity(tirray, verray):
        plt.plot(tirray,verray)
        plt.ylabel('velocity')
        plt.xlabel('total time')
        plt.title('velocity by time')
        plt.show()
    @staticmethod
    def height(tirray,herray):
        plt.plot(tirray,herray)
        plt.ylabel('height')
        plt.xlabel('total time')
        plt.title('height by time')
        plt.show()
print("insert rocket mass (kg)")
mass=float(input())
print("insert fuel mass (kg)")
fuel=float(input())
print("insert total impulse (N/s)")
total_impulse=float(input())
print("insert fuel burning time (s)")
ALT=float(input())
print ("insert angle on start")
angle=float(input())
angle=math.radians(angle)
g=9.8
horizontalvelocity=0.0
verticalvelocity=0.0
height=0.0
dtime=0.001
time=0.0
verticalacelleration=0.0
horizontalacelleration=0.0
distance=0.0
power=total_impulse/ALT
mass= mass+fuel
dfuel=fuel/ALT*dtime
maxheight=height
maxvelocity=0.0
maxacelleration=0.0
value=[]
herray= []
tirray=[]
derray=[]
aarray=[]
verray=[]
iteration=0
Cx=0.25
r=0.03
h=1
airdensity=1.3
volume=math.pi*(r**2)*h
R=0
while(height>=0):
    maxvelocity=max(maxvelocity, math.sqrt((horizontalvelocity**2)+(verticalvelocity**2)))
    maxacelleration=max(maxacelleration, math.sqrt((horizontalacelleration**2)+(verticalacelleration**2)))
    maxheight=max(maxheight, height)

    if(iteration>1):
        verticalacelleration=(power*math.cos(angle)-(R*(verticalvelocity/math.sqrt((horizontalvelocity**2)+(verticalvelocity**2))))/mass)-g
        horizontalacelleration=power*math.sin(angle)-(R*(horizontalvelocity/math.sqrt((horizontalvelocity**2)+(verticalvelocity**2))))/mass
        R=Cx*((volume**(2/3))*(airdensity*((horizontalvelocity**2)+(verticalvelocity**2))/2))
    else:
        verticalacelleration=power*math.cos(angle)/mass-g
        horizontalacelleration=power*math.sin(angle)/mass
    horizontalvelocity=horizontalvelocity+(horizontalacelleration*dtime)
    verticalvelocity=verticalvelocity+(verticalacelleration*dtime)
    height= height+(verticalvelocity*dtime)
    distance=distance+(horizontalvelocity*dtime)
    time+=dtime
    value=[verticalacelleration,verticalvelocity, horizontalacelleration,horizontalvelocity,height,distance]
    herray.append(height)
    derray.append(distance)
    aarray.append(verticalacelleration)
    verray.append(verticalvelocity)
    tirray.append(time)
    mass=mass-dfuel
    if (time>=ALT and power!=0):
        power=0
    iteration+=1
print ("max velocity " + str(maxvelocity) + "    max height " + str(maxheight) + "    max acelleration " + str(maxacelleration)+ "    flight time " + str(time)+ "    distance " + str(distance))
output.every_value(tirray,aarray,verray,herray)
output.trace(derray,herray)
