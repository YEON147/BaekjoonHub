N = int(input())
arr = [[0]*100 for _ in range(100)]
total = 0
for _ in range(N):
    c, r = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            if not arr[i][j]:
                arr[i][j] = 1
                total += 1
print(total)
