def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = 1
        else:
            dic[c[1]] += 1

    for v in dic.values():
        answer *= (v+1)

    return answer-1