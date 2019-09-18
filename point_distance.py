# Calculates distance between two points given their coordinates
def point_distance(x0, y0, x1, y1):
    distance = ((x1-x0)**2+(y1-y0)**2)**0.5
    print(distance)

point_distance(0,0,3,4)