def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    return [sum(score.get(name, 0) for name in r) for r in photo]