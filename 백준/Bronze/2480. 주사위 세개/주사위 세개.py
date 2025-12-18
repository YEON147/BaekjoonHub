num = list(map(int, input().split()))
count = [0, 0, 0, 0, 0, 0, 0]
ans = 0

for n in num:
  count[n] += 1

if max(count) == 3:
  ans = 10000 + num[0]*1000
elif max(count) == 2:
  ans = 1000 + count.index(max(count))*100
else:
  ans = max(num)*100
print(ans)