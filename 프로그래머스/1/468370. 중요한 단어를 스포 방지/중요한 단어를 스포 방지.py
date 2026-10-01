def solution(message, spoiler_ranges):
    answer = []
    new = list(message)

    # 바꾸기 전 단어
    sentence = message.split(' ')         

    # 마스킹
    for s, e in spoiler_ranges:
        for x in range(s, e + 1):
            if new[x] != ' ':
                new[x] = '*'

    words = ''.join(new).split(' ')

    for i in range(len(sentence)):
        if '*' in words[i]:          
            words[i] = sentence[i]
            if words.count(words[i]) < 2: 
                answer.append(sentence[i])
    return len(answer)                     