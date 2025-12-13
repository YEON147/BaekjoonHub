N, M = map(int, input().split())
num = list(map(int, input().split()))
ans = set()

def seq(start, depth, new):
    if depth == M:
        ans.add(tuple(sorted(new)))
        return
    for i in range(start, N):
        new.append(num[i])
        seq(i, depth+1, new)
        new.pop()

seq(0, 0, [])
for n in sorted(ans):
    print(*n)