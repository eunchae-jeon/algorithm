def solution(citations):
    citations.sort()
    answer = 0

    for i, c in enumerate(citations):
        answer = max(answer, min(len(citations)-i, c))
    return answer

