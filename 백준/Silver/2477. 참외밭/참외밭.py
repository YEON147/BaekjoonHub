N = int(input())
square = [[] for _ in range(5)]
ground = []
minus = 1
big = 1
for _ in range(6):
    d, length = map(int, input().split())
    square[d].append(length)
    ground.append([d, length])

for i in range(5):
    if len(square[i]) == 1:
        big *= square[i][0]

for g in range(6):
    if ground[(g+5)%6][0] == ground[(g+1)%6][0]:
        minus *= ground[g][1]

print((big-minus)*N)
