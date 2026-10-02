from collections import deque
def solution(maps):
    r, c = len(maps), len(maps[0])
    dist = [[0]*c for _ in range(r)]
    
    queue = deque([(0,0)])
    dist[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # 우하좌상
            nx, ny = x+dx, y+dy
            
            if nx < 0 or nx >= r or ny < 0 or ny >= c: # 맵밖일때
                continue 
            if maps[nx][ny] == 0:   # 벽일때
                continue
            if dist[nx][ny] != 0:   # 이미 방문 했을 때
                continue
            
            queue.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    ans = dist[r-1][c-1]   
    return  ans if ans else -1