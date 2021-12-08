#!/usr/bin/python3

def rotateR(x, y):
	print('ROTATE R')
	oldx = x
	newx = y
	newy = -oldx
	return [newx, newy]

def rotateL(x, y):
	print('ROTATE L')
	oldy = y
	newy = x
	newx = -oldy
	return [newx, newy]
	
programFile = open('input', 'r')
instructions = programFile.readlines()

x = 0
y = 0
wx = 10
wy = 1

for instruction in instructions:
	action = instruction[0:1]
	quantity = int(instruction[1:-1])
	print('Action '+ action +', quantity '+ str(quantity))
	if (action == 'F'):
		x += quantity * wx
		y += quantity * wy
	if (action == 'R'):
		for n in range(0, int(quantity/90)):
			wx, wy = rotateR(wx, wy)
	if (action == 'L'):
		for n in range(0, int(quantity/90)):
			wx, wy = rotateL(wx, wy)

	if (action == 'N'):
		wy += quantity
	if (action == 'E'):
		wx += quantity
	if (action == 'S'):
		wy -= quantity
	if (action == 'W'):
		wx -= quantity

	print('Position '+ str(x) +', '+ str(y))
	print('Waypoint '+ str(wx) +', '+ str(wy) + '\n\n')

print('Finished at '+ str(x) +', '+ str(y))
print('Sum '+ str(abs(x) + abs(y)))
programFile.close();
