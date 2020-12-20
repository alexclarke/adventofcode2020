#!/usr/bin/python3
import math

def search(rowSpec, l, r, lC, rC):
    seat = 0
    for c in rowSpec:
        span = r - l
        if c == lC:
            r -= math.ceil(span / 2)
            seat = r
        elif c == rC:
            l += math.ceil(span / 2)
            seat = l
    return seat

seatsFile = open('input', 'r')

seatsLines = seatsFile.readlines()

high = 0 
seatNumbers = []

for seatLine in seatsLines:
    rowSpec, colSpec = seatLine[:7], seatLine[7:]
    row = search(rowSpec, 0, 127, 'F', 'B')
    col = search(colSpec, 0, 7, 'L', 'R')
    num = (row * 8) + col
    seatNumbers.append(num)
    if num > high:
        high = num
    print('row '+rowSpec, 'col '+colSpec +' defines seat ('+ str(row) +','+ str(col) + ') with number '+ str(num))

print(high)

seatNumbers.sort()
index = 1
while True:
    previousSeat = seatNumbers[index-1] 
    current = seatNumbers[index]
    nextSeat = seatNumbers[index+1] 

    print(str(previousSeat) +' - '+ str(current) +' - '+ str(nextSeat))

    if current - previousSeat > 1:
        print('My seat '+ str(current-1))

    index += 1
    if index > len(seatNumbers):
        exit()

