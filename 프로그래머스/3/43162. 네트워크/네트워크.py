def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(start):
        visited[start] = 1                 # ① 방문 표시
        for j in range(n):                 # ② 열 순회(연결된 점 찾기)
            if computers[start][j] == 1 and visited[j] == 0:
                dfs(j)                     # ③ 연결된 미방문 컴퓨터로 들어감

    for i in range(n):                     # ④ 바깥에서 각 행 순회
        if visited[i] == 0:
            answer += 1                    # ⑤ 연결안된 네트워크 or 연결된 네트워크 시작점 count
            dfs(i)                         # ⑥ 시작점부터 연결 컴퓨터 찾기

    return answer
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))