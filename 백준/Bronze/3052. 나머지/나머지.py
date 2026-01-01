mod = set()
for _ in range(10):
    n = int(input())
    mod.add(n%42)
print(len(mod))