P = int(input())
for _ in range(P):
    ans = 0
    li = []
    tc, *num = list(map(int, input().split()))
    for i in range(20):
        for j in range(i):
            if li[j] > num[i]:
                li.insert(j, num[i])
                ans += i-j
                break
        else:
            li.append(num[i])
    print(tc, ans)