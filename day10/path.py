#!/usr/bin/python3

import functools

programFile = open('input', 'r')
xmasLines = [*map(lambda x: int(x), programFile.readlines())]

jolts = [0, *sorted(xmasLines), max(xmasLines)+3]
print('Ordered adapters \n'+ str(jolts) +'\n')

i = 0
paths = []
for jolt in jolts:
    variants = 0
    for j in range(1, 4 if i < len(jolts)-3 else len(jolts)-i):
        if jolts[i+j] <= jolt + 3:
            variants += 1
    paths.append(variants)
    i += 1
print('Got paths from each adapter \n'+ str(paths) +'\n')

pathV = []
cv = 0
elements = 0
for path in paths:
    if path == 1 and elements > 0:
        if elements > 1:
            pathV.append(cv - 1)
        else:
            pathV.append(cv)
        cv = 0
        elements = 0
    elif elements > 0:
        cv += path
        elements += 1
    elif path != 1:
        elements = 1
        cv = path
print('Got varying paths sections \n'+ str(pathV))
print(functools.reduce(lambda x, y: x * y, pathV))

programFile.close()
