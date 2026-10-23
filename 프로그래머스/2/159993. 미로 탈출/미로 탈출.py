from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    D = [[0,1], [1,0], [0,-1], [-1,0]]  #우하좌상
    # 최소 탈출 시간
    # 레버 내리고 탈출구로
    # 1. 시작 - 레버
    # 2. 레버 - EXIT
    
    sx, sy = -1, -1
    lx, ly = -1, -1
    for i in range(N):
        if "S" in maps[i]:
            sx, sy = i, maps[i].index("S")
        if "L" in maps[i]:
            lx, ly = i, maps[i].index("L")
    
    def bfs(sx, sy, target):
        q = deque([(sx,sy)])
        visited = [[0]*M for _ in range(N)]
        while q:
            x, y = q.popleft()
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if nx<0 or nx>=N or ny<0 or ny>=M:
                    continue
                if visited[nx][ny] or maps[nx][ny] == "X":
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if maps[nx][ny] == target:
                    return visited[nx][ny]
        return -10000000
    toL = bfs(sx, sy, "L")
    toE = bfs(lx, ly, "E")
    ans = toL + toE
    return ans if ans > 0 else -1