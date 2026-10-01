def solution(message, spoiler_ranges):
    masked = [False] * len(message)
    for s, e in spoiler_ranges:
        for x in range(s, e + 1):
            masked[x] = True

    spoiled, normal = set(), set()
    i = 0
    for word in message.split(' '):
        j = i + len(word)
        if any(masked[i:j]):
            spoiled.add(word)
        else:
            normal.add(word)
        i = j + 1  # 공백 한 칸 건너뜀

    return len(spoiled - normal)