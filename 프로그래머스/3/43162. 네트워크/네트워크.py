def solution(n, computers):
    ans = 0
    visited = [0]*n
    
    def dfs(start):
        visited[start] = 1
        for j in range(n):
            if not visited[j] and computers[start][j]:
                dfs(j)
        return
    for i in range(n):
        if not visited[i]:
            ans += 1
            dfs(i)
        
    return ans