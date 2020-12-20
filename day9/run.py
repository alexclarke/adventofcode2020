#!/usr/bin/python3

programFile = open('input', 'r')
xmasLines = programFile.readlines()

i = 25

for line in xmasLines[i:]:

    prev25 = list(map(lambda x: int(x), xmasLines[i-25:i]))
    if not len(prev25) == 25: exit()

    print(prev25)
    found = False

    for p in prev25:
        for pp in prev25:
            if p + pp == int(line):
                found = True

    if not found:
        print('Never found '+ line)
        exit()
    else:
        print('Found '+ line)

    i += 1


programFile.close()
