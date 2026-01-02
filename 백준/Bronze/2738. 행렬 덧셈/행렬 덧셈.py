N, M = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]

new = [list(map(sum, zip(arr1, arr2))) for arr1, arr2 in zip(arr1, arr2)]

for line in new:
    print(*line)