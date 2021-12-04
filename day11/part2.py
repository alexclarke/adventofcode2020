#!/usr/bin/python3

def findVisibleSeat(x, y, addVertical, addHorizontal, seats):
	currX = x
	currY = y
	while True:
		currX = currX + addHorizontal;
		currY = currY + addVertical;
		if (currX < 0 or currY < 0 or currY >= len(seats) or currX >= len(seats[0])):
			return None
		if seats[currY][currX] != '.':
			return seats[currY][currX]
			

def getVisibleSeats(x, y, seats):
		visibleSeats = []
		for addVertical in range(-1, 2):
			for addHorizontal in range(-1, 2):
				if (not(addVertical == 0 and addHorizontal == 0)):
					visibleSeat = findVisibleSeat(x, y, addVertical, addHorizontal, seats)
					if visibleSeat:
						visibleSeats.append(visibleSeat)
		return visibleSeats

def change(seat, visibleSeats):
		if seat == 'L' and not visibleSeats.count('#'):
				return '#'
		if seat == '#' and visibleSeats.count('#') >= 5:
				return 'L'
		return None

programFile = open('input', 'r')
seatLines = programFile.readlines()
seats = [[char for char in line.strip()] for line in seatLines]

print('Got '+ str(len(seats)) +' rows of seats with '+ str(len(seats[0])) +' seats in each row')

for it in range(0, 100):
		visibleSeats = [[getVisibleSeats(aSI, aRI, seats) for aSI, s in enumerate(r)] for aRI, r in enumerate(seats)]
		changeCount = 0
		for y, seatRow in enumerate(seats):
				for x, seat in enumerate(seatRow):
						newSeat = change(seat, visibleSeats[y][x])
						if newSeat: 
								seats[y][x] = newSeat
								changeCount += 1
		print('Iteration '+ str(it) +' produced '+ str(changeCount) +' changes', end='')
		print('... and '+ str(sum(x.count('#') for x in seats)) +' seats occupied')

programFile.close()
