A = int(input())
B = list(map(int, input()))

a = A*B[-1]
b = A*B[1]
c = A*B[0]
d = a+b*10+c*100
for ans in [a, b, c, d]:
  print(ans)