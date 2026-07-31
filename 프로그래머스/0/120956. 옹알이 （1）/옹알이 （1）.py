def solution(babbling):
    ans = 0
    for i in babbling:
        str = i
        str = str.replace("aya", "...")
        str = str.replace("ye", "..")
        str = str.replace("woo", "...")
        str = str.replace("ma", "..")
        if str == "."*len(i):
            ans +=1
    return ans