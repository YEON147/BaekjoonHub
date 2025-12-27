import sys
from sys import stdin

N = int(stdin.readline())
for t in range(1, N+1):
  a, b = map(int, sys.stdin.readline().split())
  print(f"Case #{t}:", a+b)



