import heapq
def solution(scoville, K):
    s = scoville
    heapq.heapify(s)
    ans = 0

    while len(s) >= 2 and s[0] < K:
        n1, n2 = heapq.heappop(s), heapq.heappop(s)
        heapq.heappush(s, n1+n2*2)
        ans += 1

    return ans if s[0] >= K else -1