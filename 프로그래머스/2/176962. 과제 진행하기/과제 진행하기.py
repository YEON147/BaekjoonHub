def solution(plans):
    def to_min(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    plans = sorted([[n, to_min(s), int(d)] for n, s, d in plans],
                   key=lambda x: x[1])

    answer = []
    stack = []  # [과목명, 남은시간]

    for i in range(len(plans) - 1):
        name, start, dur = plans[i]
        gap = plans[i + 1][1] - start   # 다음 과제 시작까지 남은 있는 시간

        if dur <= gap:
            answer.append(name)
            gap -= dur
            # 남는 시간으로 최근에 멈춘 과제부터 처리
            while stack and gap > 0:
                n, rem = stack.pop()
                if rem <= gap:
                    answer.append(n)
                    gap -= rem
                else:
                    stack.append([n, rem - gap])
                    gap = 0
        else:
            stack.append([name, dur - gap])

    # 마지막 과제
    answer.append(plans[-1][0])
    # 남은 과제
    while stack:
        answer.append(stack.pop()[0])

    return answer