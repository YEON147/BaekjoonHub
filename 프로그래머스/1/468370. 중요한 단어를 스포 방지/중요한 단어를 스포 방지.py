def solution(message, spoiler_ranges):
    answer = 0
    new = list(message)

    # 바꾸기 전 단어
    sentence = list(message.split(' '))

    # 마스킹
    for s, e in spoiler_ranges:
        for x in range(s, e + 1):
            if new[x] != ' ':
                new[x] = '*'

    words = ''.join(new).split(' ')

    for i in range(len(sentence)):
        if words[i].count('*'):
            words[i] = sentence[i]
            if words.count(words[i]) < 2:
                print(sentence[i])
                answer += 1
    return answer