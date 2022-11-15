g=10
velocity=0.0
mass= 1.1
power=50
height=0.0
dtime=0.001
temp=0.0
first= True
i=0
print (" insert acelleration lasting time")
ALT=float(input())
while(True):
    maxheight=height
    acelleration=(power/mass)-g
    velocity=velocity+(acelleration*dtime)
    height= height+(velocity*dtime)
    temp+=dtime
    print(str(temp) +"      "+ str(height) +"        "+ str(velocity))
    if (temp>=ALT):
        power=0
        
    if(maxheight>height and first):
        print ("max heigth" + str(maxheight))
        first=False
    if (height<=0 and i>1):
        print (str(velocity) + "    " + str(maxheight))
        break
    i+=1
