N, M = map(int, input().split())
pick = [0]*(N+1)
new = []
def seq(depth, start):
    if depth == M:
        print(*new)
        return
    for i in range(start, N+1):
        if not pick[i]:
            pick[i] = 1
            new.append(i)
            seq(depth+1, i+1)
            new.pop()
            pick[i] = 0
seq(0, 1)