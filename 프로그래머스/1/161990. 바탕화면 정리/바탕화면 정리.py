def solution(wallpaper):
    N, M = len(wallpaper), len(wallpaper[0])
    reversed = list(map(list, zip(*wallpaper)))

    def findstart(n, arr):
        for i in range(n):
            if "#" in arr[i]:
                return i

    def findend(n, arr):
        for i in range(n-1, -1, -1):
            if "#" in arr[i]:
                return i+1
            
    sx, sy = findstart(N, wallpaper), findstart(M, reversed)
    ex, ey = findend(N, wallpaper), findend(M, reversed)
    return [sx, sy, ex, ey]