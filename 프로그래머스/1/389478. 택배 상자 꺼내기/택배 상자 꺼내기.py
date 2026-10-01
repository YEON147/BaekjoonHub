def solution(n, w, num):
    ans = 0
    while num <= n:
        ans += 1
        k = (num - 1) % w      # 이 상자가 자기 층에서 몇 번째로 놓였는지 (0부터)
        num += 2 * (w - k) - 1 # 바로 위 상자 번호로 점프
    return ans