from collections import deque
def solution(maps):
    # 최단거리 | 출발: (0,0) 도착: (4,4)
    N, M = len(maps), len(maps[0])
    answer = 0
    dist = [[0]*M for _ in range(N)]
    D = [[0,1], [1,0], [0,-1], [-1,0]]  #우하좌상

    q = deque([(0,0)])
    dist[0][0] = 1
    while q:
        x, y = q.popleft()
        
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            # 맵 범위 밖일때
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽이거나 방문한 곳일때
            if maps[nx][ny] == 0 or dist[nx][ny]:
                continue
            # 이전거리 + 1
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))
            if [nx, ny] == [N-1, M-1]:
                return dist[nx][ny]
    return -1