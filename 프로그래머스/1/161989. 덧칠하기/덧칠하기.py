def solution(n, m, section):
    ans = 0
    painted = 0
    for i in section:
        if painted < i:
            painted = i + (m-1)
            ans += 1
        if painted > n: break
    return ans