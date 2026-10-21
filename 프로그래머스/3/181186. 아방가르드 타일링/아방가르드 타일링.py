
def solution(n):
    MOD = 1_000_000_007

    dp = [0, 1, 3, 10, 23, 62, 170]

    if n < 7:
        return dp[n]

    for i in range(7, n + 1):
        dp.append(
            (dp[i - 1]
             + 2 * dp[i - 2]
             + 6 * dp[i - 3]
             + dp[i - 4]
             - dp[i - 6]) % MOD
        )

    return dp[n]
