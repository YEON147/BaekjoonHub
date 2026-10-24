def solution(k, dungeons):
    N = len(dungeons)
    visited = [False] * N
    answer = 0

    def dfs(k, count):
        nonlocal answer
        answer = max(answer, count)

        for j in range(N):
            need, cost = dungeons[j]
            if not visited[j] and k >= need:
                visited[j] = True
                dfs(k - cost, count + 1)
                visited[j] = False

    dfs(k, 0)
    return answer