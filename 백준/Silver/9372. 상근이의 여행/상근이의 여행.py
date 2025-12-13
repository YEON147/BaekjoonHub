T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(M)]

    print(N-1)