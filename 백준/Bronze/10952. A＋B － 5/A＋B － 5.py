finished = False
while not finished:
    a, b = map(int, input().split())
    if a==0 and b==0:
        finished = True
        break
    print(a+b)