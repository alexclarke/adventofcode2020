#!/usr/bin/python3

programFile = open('input', 'r')
xmasLines = [*map(lambda x: int(x), programFile.readlines())]

jolts = sorted(xmasLines)

diff1Count = 1
diff3Count = 1

i = 0

for jolt in jolts:
    if i > 0:
        diff = jolt - jolts[i-1]
        if diff == 1:
            diff1Count += 1
            print('One jolt: '+ str(jolt) +' minus '+ str(jolts[i-1]))
        elif diff == 3:
            diff3Count += 1
            print('Three jolts: '+ str(jolt) +' minus '+ str(jolts[i-1]))
        else:
            exit()
    i += 1

print(str(diff1Count) +' differences of one jolt')
print(str(diff3Count) +' differences of three jolts')

ans = diff1Count * diff3Count

print(ans)


programFile.close()
