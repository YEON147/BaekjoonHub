n = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    cnt = 0
    while V >= P:
        V -= P
        cnt += L
    if L > V:
        cnt += V
    else:
        cnt += L
    print(f"Case {n}:", cnt)
    n += 1