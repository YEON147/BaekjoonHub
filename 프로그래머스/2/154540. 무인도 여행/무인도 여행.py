def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    visited = [[0]*M for _ in range(N)]
    D = [[0,1], [1,0], [0,-1], [-1,0]] #우하좌상
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
                        nx, ny = x + dx, y + dy
                        if nx<0 or ny <0 or nx>=N or ny >=M:
                            continue
                        if visited[nx][ny] or maps[nx][ny] == "X":
                            continue
                        stack.append([nx, ny])
                        visited[nx][ny] = 1
                        total += int(maps[nx][ny])
                answer.append(total)
    # for l in visited:
    #     print(l)

    return sorted(answer) if answer else [-1]