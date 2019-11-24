points = []
tags = []


def get_num(num):
	if num == 1:
		return "2"
	elif num == 2:
		return "12"
	if num%2 == 0:
		middle = "2"
	else:
		middle = "1"
	return get_num(num - 1)[1:][::-1] + middle + get_num(num - 1)[:-1][::-1]

'''
num = get_num(5)
print(num)
'''

def tag_num(series,order):
	filled_count = 0
	numbers = {key: None for key in range(1,(2**order) + 1)}
	rank =1
	if int(series[0]) == 2:
		for key in range(1,4):
			numbers[key] = (2,rank)
			rank+=1
		filled_count += 3
	elif int(series[0]) == 1:
		for key in range(1,2):
			numbers[key] = (1,1)
		filled_count += 1
	index = 1
	while index < len(series)-1:
		solo_number = int(series[index])
		if solo_number == 1:
			try:
				if int(series[index]) == int(series[index + 1]) == int(series[index + 2]) == 1:
					rank = 1
					for key in range(filled_count+1,filled_count +1 +10):
						numbers[key] = (3,rank)
						rank += 1
					filled_count += 10
					index += 3
					continue
				else:
					rank=1
					for key in range(filled_count+1,filled_count +1 +2):
						numbers[key] = (1,rank)
						rank+=1
					filled_count += 2
					index += 1
					continue
			except IndexError:
				rank = 1
				for key in range(filled_count+1,filled_count +1 +2):
					numbers[key] = (1,rank)
					rank+=1
				filled_count += 2
				index +=1
				continue
		elif solo_number == 2:
			rank =1
			for key in range(filled_count+1,filled_count +1 +6):
				numbers[key] = (2,rank)
				rank+=1
			filled_count += 6
			index +=1
	rank =1
	for key in range(filled_count+1,(2**order) + 1):
		numbers[key] = (int(series[-1]),rank)
		rank +=1
	return numbers


print(tag_num(get_num(5),5))



'''
Code for generating the coordinates
'''
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
		# rotate 135
		for point in shrinkedpoints:
			rotatedpoints.append(rotate((0,0), point, math.radians(-135)))
		# shift rotated to new position
		for point in rotatedpoints:
			finalpoints.append(shift(point, [length/2, length/2]))
		finalpoints = finalpoints[::-1] + transformx(finalpoints)
		return finalpoints

def solve_obstacle(order,obstacle):
	points=curve(order,6)
	tags = tag_num(get_num(order),order)
	obstacle -= 1
	# points  =  list(points.values())
	if tags[obstacle+1][0] == 1:
		if tags[obstacle+1][1] == 1:
			midarray = [points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==2:
			midarray = [points[obstacle-2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
	if tags[obstacle+1][0] == 2:
		if tags[obstacle+1][1] == 1:
			midarray = [points[obstacle+6],points[obstacle+5],points[obstacle+4],points[obstacle+3],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==2:
			midarray = [points[obstacle-2],points[obstacle+5],points[obstacle+4],points[obstacle+3],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] == 3:
			midarray = [points[obstacle-2],points[obstacle-3],points[obstacle+4],points[obstacle+3],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==4:
			midarray = [points[obstacle-2],points[obstacle-3],points[obstacle-4],points[obstacle+3],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] == 5:
			midarray = [points[obstacle-2],points[obstacle-3],points[obstacle-4],points[obstacle-5],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==6:
			midarray = [points[obstacle-2],points[obstacle-3],points[obstacle-4],points[obstacle-5],points[obstacle-6],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
	if tags[obstacle+1][0] == 3:
		if tags[obstacle+1][1] == 1:
			midarray = [points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==2:
			midarray = [points[obstacle-2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] == 3:
			midarray = [points[obstacle-2],points[obstacle-3],points[obstacle-4],points[obstacle+9],points[obstacle+8],points[obstacle+7],points[obstacle+6],points[obstacle+5],points[obstacle+4],points[obstacle+3],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==4:
			midarray = [points[obstacle-2],points[obstacle-3],points[obstacle-4],points[obstacle-5],points[obstacle+8],points[obstacle+7],points[obstacle+6],points[obstacle+5],points[obstacle+4],points[obstacle+3],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] == 5:
			midarray = [points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==6:
			midarray = [points[obstacle-2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] == 7:
			midarray = [points[obstacle-2],points[obstacle-3],points[obstacle-4],points[obstacle-5],points[obstacle-6],points[obstacle-7],points[obstacle-8],points[obstacle+5],points[obstacle+4],points[obstacle+3],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==8:
			midarray = [points[obstacle-2],points[obstacle-3],points[obstacle-4],points[obstacle-5],points[obstacle-6],points[obstacle-7],points[obstacle-8],points[obstacle-9],points[obstacle+4],points[obstacle+3],points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] == 9:
			midarray = [points[obstacle+2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
		elif tags[obstacle+1][1] ==10:
			midarray = [points[obstacle-2],points[obstacle+1]]
			points = points[:obstacle] + midarray + points[obstacle+2:]
	return points


import random
order = 7
obstacle = random.choice(range(4,2**order - 2))
solved_points = solve_obstacle(order,obstacle)
print('obstacle - ',obstacle)
plot(solved_points)




