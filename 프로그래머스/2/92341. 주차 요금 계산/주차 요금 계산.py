import math
from collections import defaultdict

def solution(fees, records):
    base_t, base_f, unit_t, unit_f = fees

    def to_min(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    in_time = {}
    total = defaultdict(int)

    for r in records:
        time, num, info = r.split()
        if info == "IN":
            in_time[num] = to_min(time)
        else:
            total[num] += to_min(time) - in_time.pop(num)

    # 출차 기록 없는 차는 23:59 출차
    for num, t in in_time.items():
        total[num] += to_min("23:59") - t
    print(total)
    answer = []
    for num in sorted(total):
        stay = total[num]
        fee = base_f
        if stay > base_t:
            fee += math.ceil((stay - base_t) / unit_t) * unit_f
        answer.append(fee)
    return answer