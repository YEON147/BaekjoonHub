N, M = map(int, input().split())
card_list = list(map(int, input().split()))

maxi = 0
for i in card_list:
    for j in card_list:
        if i == j:
            continue
        for k in card_list:
            if i ==k or j ==k:
                continue
            elif maxi < i+j+k <= M:
                maxi = i+j+k
print(maxi)