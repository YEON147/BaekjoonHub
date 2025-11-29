def bingo(arr):
    cnt = 0
    for n in range(5):
        if arr[n].count(0) == 5:
            cnt += 1
    return cnt
def cross(arr):
    cnt = 0
    for m in range(5):
        if arr[m][m] != 0:
            return 0
    cnt = 1
    return cnt
def cross_2(arr):
    cnt = 0
    for x in range(5):
        if arr[x][5-1-x] != 0:
            return 0
    cnt = 1
    return cnt
iron = []
mic = []
for _ in range(5):
    iron.append(list(map(int, input().split())))
for _ in range(5):
    mic.extend(list(map(int, input().split())))
iron_col = list(map(list, zip(*iron)))

BINGO = False
count = 0
for i in mic:
    if BINGO:
        break
    count += 1
    for r in range(5):
        if i in iron[r]:
            s = iron[r].index(i)
            iron[r][s] = 0
            iron_col[s][r]=0
            break
    if count >= 12:
        if bingo(iron) + bingo(iron_col) + cross(iron)+ cross_2(iron) >=3:
            BINGO = True
print(count)