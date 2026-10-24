def solution(dirs):
    D = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    x, y = 0, 0
    roads = set()

    for d in dirs:
        dx, dy = D[d]
        nx, ny = x + dx, y + dy
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
        roads.add((x, y, nx, ny))
        roads.add((nx, ny, x, y))  
        x, y = nx, ny

    return len(roads) // 2