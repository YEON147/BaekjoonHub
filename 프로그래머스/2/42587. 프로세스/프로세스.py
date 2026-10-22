from collections import deque

def solution(priorities, location):
    q = deque((p, i) for i, p in enumerate(priorities))
    answer = 0

    while q:
        p, idx = q.popleft()

        # 남은 문서 중 더 높은 우선순위가 있는 경우
        if any(p < other_p for other_p, _ in q):
            q.append((p, idx))
        else:
            answer += 1

            if idx == location:
                return answer