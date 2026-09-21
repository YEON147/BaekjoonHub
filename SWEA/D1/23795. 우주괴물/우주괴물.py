T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [[0,1], [1,0], [0,-1], [-1,0]]

    x, y = 0, 0
    for r in range(N):
        if arr[r].count(2):
            x, y = r, arr[r].index(2)
            break
    for dx, dy in P:
        for n in range(1, N):
            ni, nj = x+dx*n, y+dy*n
            if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == 1:
                break
            arr[ni][nj] = 1

    cnt = 0
    for c in range(N):
        cnt += arr[c].count(0)

    print(f"#{tc} {cnt}")
