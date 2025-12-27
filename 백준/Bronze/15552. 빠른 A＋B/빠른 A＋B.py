import sys
from sys import stdin

N = int(stdin.readline())
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)