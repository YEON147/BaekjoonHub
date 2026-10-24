def solution(keymap, targets):
    # 키맵 중에 더 가까운 인덱스 문자열 찾기
    def find_close(t):
        idx = []
        for key in keymap:
            if t in key:
                idx.append(key.index(t)+1)
        return min(idx) if idx else -1000000

    ans = [] 
    for target in targets:
        total = 0
        for t in target:
            total += find_close(t)
        if total < 0:
            ans.append(-1)
        else:
            ans.append(total)
        
    return ans