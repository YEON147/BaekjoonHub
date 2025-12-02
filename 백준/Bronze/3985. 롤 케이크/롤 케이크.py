L = int(input())
N = int(input())
cake = [0] * (L+1)
P = [0] * N
maxi = [0, 0]
for i in range(N):
    s, e = map(int, input().split())
    if (e-s) > maxi[1] :
        maxi[0], maxi[1] = i+1, e-s
    for c in range(s, e+1):
        if not cake[c]:
            cake[c] = 1
            P[i] += 1
ans = P.index(max(P)) + 1
print(maxi[0])
print(ans)