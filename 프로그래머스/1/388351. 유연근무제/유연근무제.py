def solution(schedules, timelogs, startday):
    # 출근 희망 시각 / 출근한 시각 / 이벤트 시작요일
    # 월: 1, 화:2, 수:3, 목:4, 금:5, 토:6, 일:7
    cnt = 0
    n = len(schedules)
    for i in range(n):
        limit = schedules[i] + 10
        if limit % 100 >= 60:
            limit += 40
        for j in range(7):
            if (startday+j)%7 in (6, 0):
                continue
            # i번째 직원의 출근시간
            if limit < timelogs[i][j]:
                break
        else:
            cnt += 1
    return cnt