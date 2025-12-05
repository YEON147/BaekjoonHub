from heapq import heappop, heappush
def prim(s):
    pq = [(0, s)]
    MST = [0] * (V+1)
    mini = 0
    while pq:
        w, n = heappop(pq)
        if not MST[n]:
            mini += w
            MST[n] = 1

            for nxt_w, nxt_n in G[n]:
                heappush(pq, (nxt_w, nxt_n))
    return mini

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))

print(prim(1))