from collections import deque
def solution(board):
    N, M = len(board), len(board[0])    
    q = deque()
    start = []
    visited = [[-1]*M for _ in range(N)]
    D = [[0,1], [1,0], [0,-1], [-1,0]]  # 우하좌상
    
    for i in range(N):
        if "R" in board[i]:
            start = [i, board[i].index("R")]
            break
            
    q.append(start)
    visited[start[0]][start[1]] = 0

    def can_move(nx, ny):
        return 0<=nx<N and 0<=ny<M and board[nx][ny] != "D"
    
    while q:
        x, y = q.popleft()
        for dx, dy in D:
            nx, ny = x, y
            # 벽만날때까지 이동
            while can_move(nx+dx, ny+dy):
                nx += dx
                ny += dy
            # 미방문 경로일때
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny]) 
            if board[nx][ny] == "G":
                return visited[nx][ny]
    return -1