# BOJ 2525
H, M = map(int, input().split())
cook = int(input())

if (M+cook) >= 60 :
  H += (M+cook)//60
  M = (M+cook)%60
else:
  M += cook
  
if H >= 24:
  H -= 24

print(H, M)