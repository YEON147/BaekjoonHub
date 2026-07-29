def solution(arr, query):
    ans = arr
    for i, n in enumerate(query):
        if i%2 == 0 :
            ans = ans[:n+1]
        else:
            ans = ans[n:]
    return ans