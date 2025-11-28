num = 1000 - int(input())

cnt = 0
while num >= 500:
    num -= 500
    cnt += 1
while num >= 100:
    num -= 100
    cnt += 1
while num >= 50:
    num -= 50
    cnt += 1
while num >= 10:
    num -= 10
    cnt += 1
while num >= 5:
    num -= 5
    cnt += 1
while num > 0:
    num -= 1
    cnt += 1

print(cnt)
