import numpy

shape = []
def circlepoints(points,radius,center):
    slice = 2 * 3.14 / points
    for i in range(points):
        angle = slice * i
        new_x = center[0] + radius*numpy.cos(angle)
        new_y = center[1] + radius*numpy.sin(angle)

        p = (new_x,new_y)
        shape.append(p)

    return shape

print(circlepoints(100,20,[0,0]))
