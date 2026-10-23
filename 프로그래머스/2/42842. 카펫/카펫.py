def solution(brown, yellow):
    MN = brown + yellow
    MplusN = (brown+4)/2
    for i in range(1, MN+1):
        if MN%i == 0:
            m, n = i, MN//i
            if m+n == MplusN:
                return [n,m]
                