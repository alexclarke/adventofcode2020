#!/usr/bin/python3

programFile = open('input', 'r')
instructions = programFile.readlines()

facing = 90
x = 0
y = 0

for instruction in instructions:
	action = instruction[0:1]
	quantity = int(instruction[1:-1])
	print('Action '+ action +', quantity '+ str(quantity))
	if (action == 'F'):
		if (facing == 0):
			y += quantity
		if (facing == 90):
			x += quantity
		if (facing == 180):
			y -= quantity
		if (facing == 270):
			x -= quantity
	if (action == 'R'):
		facing += quantity
		facing = facing % 360
	if (action == 'L'):
		facing -= quantity
		facing = facing % 360
	if (action == 'N'):
		y += quantity
	if (action == 'E'):
		x += quantity
	if (action == 'S'):
		y -= quantity
	if (action == 'W'):
			x -= quantity
	print('At '+ str(x) +', '+ str(y) +' facing '+ str(facing) +"\n\n")

print('Finished at '+ str(x) +', '+ str(y))
print('Sum '+ str(abs(x) + abs(y)))
programFile.close();
