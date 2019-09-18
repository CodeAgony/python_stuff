# Calculates distance between two points given their coordinates
def point_distance(x0, y0, x1, y1):
    distance = ((x1-x0)**2+(y1-y0)**2)**0.5
    print(distance)
    return distance


# Accepts coordinates of 3 verticles of triangle and prints out the area after calculating it by Heron's formula given sides of triangle
def triangle_area(x0,y0,x1,y1,x2,y2):
    side1 = point_distance(x0,y0,x1,y1)
    side2 = point_distance(x1,y1,x2,y2)
    side3 = point_distance(x2,y2,x0,y0)
    semiper = (side1+side2+side3)/2
    area = (semiper*(semiper-side1)*(semiper-side2)*(semiper-side3))**0.5
    print("A triangle with vertices ({},{}), ({},{}), and ({},{}) has an area of {}".format(x0,y0,y1,y1,x2,y2,area))


triangle_area(-2, 4, 1, 6, 2, 1)