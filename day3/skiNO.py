import fileinput

r = 0
c = 0
ans = 0

G = []
for line in fileinput.input():
    G.append(list(line.strip()))


while r+1 < len(G):
    c += 3
    r += 1
    print('On '+ str(r))
    if G[r][c%len(G[r])] == '#':
        ans += 1

print(ans)
