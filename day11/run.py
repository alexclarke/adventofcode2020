#!/usr/bin/python3

def getAdjacents(x, y, lines):
    adjacents = []
    if y > 0:
        if x > 0:
            adjacents.append(lines[y-1][x-1]) 
        adjacents.append(lines[y-1][x]) 
        if x < (len(lines[y-1])-1):
            adjacents.append(lines[y-1][x+1]) 
    if x > 0:
        adjacents.append(lines[y][x-1]) 
    if x < (len(lines[y])-1):
        adjacents.append(lines[y][x+1]) 
    if y < (len(lines)-1):
        if x > 0:
            adjacents.append(lines[y+1][x-1]) 
        adjacents.append(lines[y+1][x]) 
        if x < (len(lines[y+1])-1):
            adjacents.append(lines[y+1][x+1])
    return adjacents

def change(seat, adjacents):
    #print('On '+ seat +' with adjacents '+ str(adjacents))
    if seat == 'L' and not adjacents.count('#'):
        return '#'
    if seat == '#' and adjacents.count('#') >= 4:
        return 'L'
    return None

programFile = open('input', 'r')
seatLines = programFile.readlines()
seats = [[char for char in line.strip()] for line in seatLines]

print('Got '+ str(len(seats)) +' rows of seats with '+ str(len(seats[0])) +' seats in each row')

for it in range(0, 100):
    adjacents = [[getAdjacents(aSI, aRI, seats) for aSI, s in enumerate(r)] for aRI, r in enumerate(seats)]
    y = 0
    changeCount = 0
    for seatRow in seats:
        x = 0
        for seat in seatRow:
            newSeat = change(seat, adjacents[y][x])
            #adjacents.append(print('On '+ seat +' with a new seat of '+ str(newSeat))
            if newSeat: 
                seats[y][x] = newSeat
                changeCount += 1
            x += 1
        y += 1
    print('Iteration '+ str(it) +' produced '+ str(changeCount) +' changes', end='')
    print('... and '+ str(sum(x.count('#') for x in seats)) +' seats occupied')

programFile.close()
