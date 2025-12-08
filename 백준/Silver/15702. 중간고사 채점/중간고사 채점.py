N, M = map(int, input().split())
score = list(map(int, input().split()))
student = [input().split() for _ in range(M)]

maxi = 0
idx = int(student[0][0])
for i in range(M):
    total = 0
    for p in range(1, N+1):
        if student[i][p] == 'O':
            total += score[p-1]
    if total == maxi and int(student[i][0]) < idx:
        idx = int(student[i][0])
    elif total > maxi:
        maxi = total
        idx = int(student[i][0])

print(idx, maxi)