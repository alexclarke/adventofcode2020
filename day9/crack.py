#!/usr/bin/python3

programFile = open('input', 'r')
xmasLines = programFile.readlines()

crack = 3199139634
i = 0

for line in xmasLines:
    sum = int(line)
    j = 1
    while sum < crack:
        sum += int(xmasLines[i+j])
        j += 1
        if sum == crack:
            nums = sorted(list(map(lambda x: int(x), xmasLines[i:i+j])))
            total = int(nums[0]) + int(nums[len(nums)-1])
            print('BOOOOM '+ str(total))

    i += 1



programFile.close()
