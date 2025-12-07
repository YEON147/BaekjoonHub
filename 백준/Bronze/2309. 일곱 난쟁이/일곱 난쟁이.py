from itertools import combinations

h = [int(input()) for _ in range(9)]

for i in combinations(h, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break