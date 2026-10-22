def solution(numbers, target):
    ans = 0
    def dfs(n, total):
        nonlocal ans
        if n == len(numbers):
            if total == target:
                ans += 1
            return
        dfs(n+1, total+numbers[n])
        dfs(n+1, total-numbers[n])

    dfs(0, 0)
    return ans