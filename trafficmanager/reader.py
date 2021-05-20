x=0
y=0
z=0
while(True):
    file = open('/home/justin/New_Carla/carla/LibCarla/source/carla/trafficmanager/data.txt', 'r')
    counter=0
    for line in file:
        for val in line.split():
            if counter== 0:
                x= val
                counter+=1
            elif counter==1:
                y= val
                counter+=1
            else:
                z = val
                counter=0

    x = float(x)
    y = float(y)
    z = float(z)

    if(((x>0.85 or x<-0.85) and (-0.1< y < 0.1 ) or (y>0.85 or y<-0.85) and (-0.1<x<0.1))):
        print("STRAIGHT")

    elif(x>0.85 and (0.1<y<0.84) or (x<-0.85 and (-0.84<y<-0.1)) or (y>0.85 and (-0.84<x<-0.1)) or (y<-0.85 and (0.1<x<0.84))):
        print("RIGHT")
    else:
        print("LEFT")
