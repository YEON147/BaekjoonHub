N = int(input())
total = 0
li = []
for _ in range(N):
    L, H = map(int, input().split())
    li.append([L, H])

li.sort(key=lambda x: x[0])
tall = max(li, key=lambda x: x[1])
idx = li.index(tall)

total += tall[1]

s = 0
for i in range(s, idx+1):
    if li[i][1] >= li[s][1]:
        total += (li[i][0]-li[s][0]) * li[s][1]
        s = i

e = N-1
for j in range(e, idx-1, -1):
    if li[j][1] >= li[e][1]:
        total += (li[e][0] - li[j][0]) * li[e][1]
        e = j

print(total)