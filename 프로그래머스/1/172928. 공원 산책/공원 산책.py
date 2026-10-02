def solution(park, routes):
    # S 시작지점 X 장애물
    EWSN = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}  # 우좌 하상
    w, h = len(park[0]), len(park)

    x, y = 0, 0
    for i in range(h):
        if 'S' in park[i]:
            x, y = i, park[i].index('S')
            break
    for route in routes:
        d, n = route.split()
        n = int(n)
        nx, ny = x, y
        for _ in range(n):
            nx += EWSN[d][0]
            ny += EWSN[d][1]
            if not (0 <= nx < h and 0 <= ny < w) or park[nx][ny] == 'X':
                break
        else:  
            x, y = nx, ny

    return [x, y]