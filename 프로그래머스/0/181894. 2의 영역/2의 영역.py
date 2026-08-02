def solution(arr):
    idx = [idx for idx, v in enumerate(arr) if v == 2]
    return arr[idx[0]:idx[-1]+1] if idx else [-1]

    