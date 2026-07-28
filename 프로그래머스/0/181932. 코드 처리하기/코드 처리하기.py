def solution(code):
    mode = 0
    ans = ""
    for i, s in enumerate(code):
        if mode == 1:
            if i % 2 != 0 and s != "1":
                ans += s
            elif s == "1":
                mode = 0
                continue
        if mode == 0:
            if i % 2 == 0 and s != "1":
                ans += s
            elif s == "1":
                mode = 1
    return ans if ans else "EMPTY"