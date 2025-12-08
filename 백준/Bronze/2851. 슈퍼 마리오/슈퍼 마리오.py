mushroom = []
for _ in range(10):
    num = int(input())
    mushroom.append(num)
total = 0
total_list = []

for i in mushroom:
    total += i
    total_list.append(total)

ans = 0
minus = 100-total_list[0]
for num in total_list:
    if abs(100-num) <= abs(minus):
        minus = 100-num
        ans = num
print(ans)