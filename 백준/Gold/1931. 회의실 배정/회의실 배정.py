import sys
input = sys.stdin.readline

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
li.sort(key=lambda x: (x[1], x[0]))
cnt = 1
e = li[0][1]

for i in range(1, N):
    if e <= li[i][0]:
        e = li[i][1]
        cnt += 1
print(cnt)