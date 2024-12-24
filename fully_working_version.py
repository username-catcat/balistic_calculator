from shutil import get_archive_formats
from socket import gaierror
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
class output:
    @staticmethod
    def every_value(tirray, aarray, verray, herray):
        plt.plot(tirray, verray, label="velocity")
        plt.plot(tirray, herray, label="height")
        plt.plot(tirray, aarray, label="acelleration")
        plt.xlabel("total time")
        plt.ylabel("value")
        plt.title("dependence by time")
        plt.legend()
        plt.show()

    @staticmethod
    def trace(derray, herray):
        plt.plot(derray, herray)
        plt.ylabel("height")
        plt.xlabel("distance")
        plt.title("trace")
        plt.show()

    @staticmethod
    def acelleration(tirray, aarray):
        plt.plot(tirray, aarray)
        plt.ylabel("acelleration")
        plt.xlabel("total time")
        plt.title("acelleration by time")
        plt.show()

    @staticmethod
    def velocity(tirray, verray):
        plt.plot(tirray, verray)
        plt.ylabel("velocity")
        plt.xlabel("total time")
        plt.title("velocity by time")
        plt.show()

    @staticmethod
    def height(tirray, herray):
        plt.plot(tirray, herray)
        plt.ylabel("height")
        plt.xlabel("total time")
        plt.title("height by time")
        plt.show()

mass = float(input("insert rocket mass (kg)\n"))
fuel = float(input("insert fuel mass (kg)\n"))
total_impulse = float(input("insert total impulse (N/s)\n"))
ALT = float(input("insert fuel burning time (s)\n"))
angle = float(input("insert angle on start\n"))
angle = math.radians(angle)
parachute=int(input("insert parachute type| 0 whether not\n 1. Dome\n 2. Circle \n 3. Flat polygon \n"))
if(parachute >0):
    S=float(input("insert parachute reduced area (m^2)\n"))
    if parachute==1:
        S-=float(input("insert parachute pole hole area (m^2)\n"))
Cds=[0.25, 0.75, 0.55, 0.65]
g = 9.81
horizontalvelocity = 0.0
verticalvelocity = 0.0
height = 0.0
dtime = 0.001
time = 0.0
verticalacelleration = 0.0
horizontalacelleration = 0.0
distance = 0.0
power = total_impulse / ALT
mass = mass + fuel
dfuel = fuel / ALT * dtime
maxheight = height
maxvelocity = 0.0
maxacelleration = 0.0
value = []
herray = []
tirray = []
derray = []
aarray = []
verray = []
iteration = 0
Cx = 0.25
r = 0.03
h = 1
airdensity = 1.3
volume = math.pi * (r**2) * h
Recrit=51*(10**-5*h)**-1.039
r = 0.03
Resistance = 0
he=0
di=0
Cf=0
kin= [
    1.46*(10**-5),
    1.52*(10**-5),
    1.58*(10**-5),
    1.65*(10**-5),
    1.71*(10**-5),
    1.79*(10**-5)
    ]
while height >= 0:
    maxvelocity = max(maxvelocity, math.sqrt((horizontalvelocity**2) + (verticalvelocity**2)))
    maxacelleration = max(maxacelleration, math.sqrt((horizontalacelleration**2) + (verticalacelleration**2)))
    maxheight = max(maxheight, height)
    if height>500:
        he=1
        if height>1000:
            he=2
            if height>1500:
                he=3
                if height>2000:
                    he=4
                    if height>2500:
                        he=5
    if iteration > 1:
        verticalacelleration = (power * math.cos(angle)- (Resistance* (verticalvelocity/ math.sqrt((horizontalvelocity**2) + (verticalvelocity**2))))/ mass) - g
        horizontalacelleration = (power * math.sin(angle)- (Resistance* (horizontalvelocity/ math.sqrt((horizontalvelocity**2) + (verticalvelocity**2))))/ mass)
        Resistance = Cx * ((volume ** (2 / 3))* (airdensity * ((horizontalvelocity**2) + (verticalvelocity**2)) / 2)) +Cf * (2*math.pi * r *h * (airdensity * ((horizontalvelocity**2) + (verticalvelocity**2)) / 2))
        if(height<maxheight):
            Resistance+= Cds[parachute] * (S* (airdensity * ((horizontalvelocity**2) + (verticalvelocity**2)) / 2))
    else:
        verticalacelleration = power * math.cos(angle) / mass - g
        horizontalacelleration = power * math.sin(angle) / mass
    horizontalvelocity = horizontalvelocity + (horizontalacelleration * dtime)
    verticalvelocity = verticalvelocity + (verticalacelleration * dtime)
    height = height + (verticalvelocity * dtime)
    distance = distance + (horizontalvelocity * dtime)
    time += dtime
    herray.append(height)
    derray.append(distance)
    aarray.append(verticalacelleration)
    verray.append(verticalvelocity)
    tirray.append(time)
    mass = mass - dfuel
    while(di<h):
        LRc=di*math.sqrt((horizontalvelocity**2) + (verticalvelocity**2))/kin[he]
        if LRc>Recrit: Cf= 0.032*(0.0000002/h)**0.2
        if LRc<10000: Cf= 0.0148
        di+=0.0001
    if time >= ALT and power != 0:
        power = 0
        dfuel = 0
    iteration += 1
print(
    f"max velocity"
    + str(maxvelocity)
    + "    max height "
    + str(maxheight)
    + "    max acelleration "
    + str(maxacelleration)
    + "    flight time "
    + str(time)
    + "    distance "
    + str(distance)
)
output.every_value(tirray, aarray, verray, herray)
output.trace(derray, herray)