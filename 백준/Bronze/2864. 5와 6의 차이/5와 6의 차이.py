a, b = input().split()
Ma = a.replace('5', '6')
Mb = b.replace('5', '6')
maxi = int(Ma) + int(Mb)

ma = a.replace('6', '5')
mb = b.replace('6', '5')
mini = int(ma) + int(mb)

print(mini, maxi)
