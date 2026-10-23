def solution(maps):
    N, M = len(maps), len(maps[0])
    D = [[0,1], [1,0], [0,-1], [-1,0]]  #우하좌상
    visited = [[0]*M for _ in range(N)]
    answer = []
    stack = []
    for i in range(N):
        for j in range(M):
            if maps[i][j].isdigit() and not visited[i][j]:
                stack.append([i, j])
                visited[i][j] = 1
                total = int(maps[i][j])
                
                while stack:
                    x, y = stack.pop()
                    for dx, dy in D:
                        nx, ny = x+dx, y+dy
                        
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                            
                        if maps[nx][ny].isdigit() and not visited[nx][ny]:
                            stack.append([nx, ny])
                            visited[nx][ny] = 1
                            total += int(maps[nx][ny])
                answer.append(total)
    return sorted(answer) if answer else [-1]