
def solution(n, wires):
    arr = [[] for _ in range(n + 1)]

    # 1. 그래프 만들기
    for s, e in wires:
        arr[s].append(e)
        arr[e].append(s)

    ans = n

    # 2. 모든 간선을 하나씩 끊어 보기
    for cut_a, cut_b in wires:
        visited = [0] * (n + 1)

        # 3. 한쪽 그룹의 송전탑 개수 세기
        def dfs(start):
            visited[start] = 1
            count = 1

            for next in arr[start]:
                # 끊은 간선이면 건너뛰기
                if {start, next} == {cut_a, cut_b}:
                    continue

                if not visited[next]:
                    count += dfs(next)

            return count
        count1 = dfs(1)
        count2 = n - count1
        ans = min(ans, abs(count1 - count2))
    return ans
