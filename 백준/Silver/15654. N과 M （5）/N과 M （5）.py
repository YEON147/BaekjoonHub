N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
pick = [0]*(N) 
new = []
def seq(depth):
    if depth == M:
        print(*new)
        return
    for i in range(N):
        if not pick[i]:
            pick[i] = 1
            new.append(num[i])
            seq(depth+1)
            new.pop()
            pick[i] = 0
seq(0)