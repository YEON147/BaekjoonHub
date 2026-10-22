from collections import deque
def solution(n, edge):
    answer = 0
    dist = [0]*(n+1)
    arr = [[] for _ in range(n+1)]

    for s, e in edge:
        arr[s].append(e)
        arr[e].append(s)
    # 1번에서 가장 멀리 떨어진 노드 

    q = deque([])
    q.append(1)
    dist[1] = 1
    while q:
        idx = q.popleft()
        for j in arr[idx]:
            if dist[j]:
                continue
            dist[j] = dist[idx] + 1
            q.append(j)

    return dist.count(max(dist))