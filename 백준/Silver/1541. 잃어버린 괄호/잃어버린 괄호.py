# BOJ_1541
num = list(input().split('-'))
total = 0
plus = 0
for i in num[:1]:
    total += sum(map(int, i.split('+')))
for j in num[1:]:
    total -= sum(map(int, j.split('+')))
print(total)