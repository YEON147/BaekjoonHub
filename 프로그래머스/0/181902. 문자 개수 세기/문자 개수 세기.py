def solution(my_string):
    ans = [0]*52
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc = "abcdefghijklmnopqrstuvwxyz"
    for s in my_string:
        idx = 0
        if s in ABC:
            idx = ABC.index(s)
            ans[idx] += 1
        else:
            idx = abc.index(s)
            ans[idx+26] += 1
    return ans