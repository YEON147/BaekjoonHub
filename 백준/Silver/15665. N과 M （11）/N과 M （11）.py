N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = set()

def seq(depth, new):
    if depth == M:
        ans.add(tuple(new))
        return
    for i in range(N):
        new.append(num[i])
        seq(depth+1, new)
        new.pop()
seq(0, [])
for n in sorted(ans):
    print(*n)