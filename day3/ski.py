#!/usr/bin/python3
import fileinput 

landscapeRows = []
for line in fileinput.input():
    landscapeRows.append(list(line.strip()))

def findTrees(across, down):
    treeCount = 0

    currentCoordinates = (0, 0)

    while True:
        currentCoordinates = (currentCoordinates[0]+down, currentCoordinates[1]+across)

        if currentCoordinates[0]+1 > len(landscapeRows): 
            return treeCount

        if landscapeRows[currentCoordinates[0]][currentCoordinates[1] % len(landscapeRows[currentCoordinates[0]])] == '#':
            treeCount += 1


first = findTrees(1,1)
second = findTrees(3,1)
third = findTrees(5,1)
fourth = findTrees(7,1)
fifth = findTrees(1,2)

print('Got '+ str(first) +' '+ str(second) +' '+ str(third) +' '+ str(fourth) +' '+ str(fifth))
result = first * second * third * fourth * fifth
print('Total '+ str(result))


