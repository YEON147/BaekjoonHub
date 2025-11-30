H, W = map(int, input().split())
arr = [input() for _ in range(H)]
ans = [[0] * W for _ in range(H)]

for r in range(H):
    idx = -1
    for c in range(W):
        if arr[r][c] == 'c':
            ans[r][c] = 0
            idx = c
        else:
            if idx != -1:
                ans[r][c] = c-idx
            else:
                ans[r][c] = -1

for line in ans:
    print(*line)