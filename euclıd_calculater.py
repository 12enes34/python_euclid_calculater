import math


def euclid_calculater(point1,point2):
    x1 , y1 = point1
    x2 , y2 = point2

    return(math.sqrt((x2-x1)**2+(y2-y1)**2))



print(euclid_calculater((0,0),(3,4)))