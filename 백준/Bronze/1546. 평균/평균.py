N = int(input())
score = list(map(int, input().split()))
avg = 0
maxi = max(score)
for i in range(N):
    avg += score[i]/maxi * 100

print(avg/N)