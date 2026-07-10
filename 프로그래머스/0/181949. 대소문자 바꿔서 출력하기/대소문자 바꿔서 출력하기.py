str = input()
ans = ''
for i in str:
    if i == i.upper():
        ans += i.lower()
    else:
        ans += i.upper()
        
print(ans)