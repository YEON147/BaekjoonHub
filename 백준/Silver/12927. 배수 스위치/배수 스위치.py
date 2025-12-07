
bulb = list(input())
N = len(bulb)
cnt = 0

for i in range(N):
    if bulb[i] == "Y":
        cnt += 1
        for j in range(N):
            if (j+1) % (i+1) == 0:
                bulb[j] = "N" if bulb[j] == "Y" else "Y"
    if ''.join(bulb) == "N"*N:
        break
print(cnt)
