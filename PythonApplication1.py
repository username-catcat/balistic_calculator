import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
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
g=10
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
herray= []
tirray=[]
derray=[]
aarray=[]
verray=[]
iteration=0

while(height>=0):
    maxvelocity=max(maxvelocity, math.sqrt((horizontalvelocity**2)+(verticalvelocity**2)))
    maxacelleration=max(maxacelleration, math.sqrt((horizontalacelleration**2)+(verticalacelleration**2)))
    maxheight=max(maxheight, height)
    verticalacelleration=power*math.cos(angle)/mass-g
    horizontalacelleration=power*math.sin(angle)/mass
    horizontalvelocity=horizontalvelocity+(horizontalacelleration*dtime)
    verticalvelocity=verticalvelocity+(verticalacelleration*dtime)
    height= height+(verticalvelocity*dtime)
    distance=distance+(horizontalvelocity*dtime)
    time+=dtime
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
plt.plot(tirray,verray, label='velocity')
plt.plot(tirray,herray, label='height')
plt.plot(tirray, aarray, label='acelleration')
plt.ylabel('height')
plt.xlabel('total time')
plt.title('height from time')
plt.legend()
plt.show()
plt.plot(derray,herray)
plt.ylabel('height')
plt.xlabel('distance')
plt.title('trace')
plt.show()
plt.plot(tirray, aarray)
plt.ylabel('acelleration')
plt.xlabel('total time')
plt.title('acelleration from time')
plt.show()
plt.plot(tirray,verray)
plt.ylabel('velocity')
plt.xlabel('total time')
plt.title('velocity from time')
plt.show()
