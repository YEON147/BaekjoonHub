N, M = map(int, input().split())
ball = [0] + [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    ball[i], ball[j] = ball[j], ball[i]
print(*ball[1:])