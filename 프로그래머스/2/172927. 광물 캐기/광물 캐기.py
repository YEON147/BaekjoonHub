def solution(picks, minerals):
    dia, iron, stn = picks[0], picks[1], picks[2]
    # 최소한의 피로도로 광물 캐기
    # 각 곡괭이는 광물 다섯개까지 캐기 가능 
    score = {"diamond": 25, "iron": 5, "stone": 1}
    answer = 0
    new = []
    N = min(sum(picks)*5, len(minerals))
    for i in range(0, N, 5):
        s = 0
        li = minerals[i:i+5]
        s += sum(score[m] for m in li)
        new.append((s, li))
    new.sort(key = lambda x : -x[0])
    for m in new:
        if dia > 0:
            dia -= 1
            answer += len(m[1])
            continue
        if iron > 0:
            iron -= 1
            d = m[1].count("diamond")
            etc = len(m[1]) - d
            answer += d*5 + etc
            continue
        stn -= 1
        d = m[1].count("diamond")
        i = m[1].count("iron")
        s = len(m[1]) - d - i
        answer += d*25 + i*5 + s
        if not stn:
            break
    return answer