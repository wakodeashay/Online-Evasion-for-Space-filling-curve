
from matplotlib import pyplot

import math

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [qx, qy]

def shift(point, origin):
	return [point[0] - origin[0], point[1] + origin[1]]

def transformx(points):
	new = []
	for point in points:
		new.append([-point[0], point[1]])
	return new

def plot(points):
	x = []
	y = []
	for point in points:
		x.append(point[0])
		y.append(point[1])
	pyplot.plot(x, y)
	pyplot.show()

def curve(order,length):
	if order == 1:
		points = [[-length/3, length/3], [+length/3, length/3]]
		return points
	else:
		rotatedpoints = []
		shrinkedpoints = []
		finalpoints = []
		# shrink points
		for point in curve(order - 1, length):
			shrinkedpoints.append([point[0]/(2**(1/2)), point[1]/(2**(1/2))])
		# print(shrinkedpoints)
		# rotate 135
		for point in shrinkedpoints:
			rotatedpoints.append(rotate((0,0), point, math.radians(-135)))
		# shift rotated to new position
		for point in rotatedpoints:
			finalpoints.append(shift(point, [length/2, length/2]))
		finalpoints = finalpoints[::-1] + transformx(finalpoints)
		# print(finalpoints)
		return finalpoints




plot(curve(9,6))
