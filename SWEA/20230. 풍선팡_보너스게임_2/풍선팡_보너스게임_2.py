T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [[0, 1], [1, 0], [0, -1], [-1, 0]] #우하좌상
    maxi = 0

    for i in range(N):
        for j in range(N):
            total = sum(arr[i])
            x, y = i, j
            for k in range(N):
                total += arr[k][j]
            total -= arr[i][j]
            maxi = max(maxi, total)
    print(f"#{tc}", maxi)
