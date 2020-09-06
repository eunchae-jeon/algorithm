def solution(n, computers):
    visit = [-1] * n
    answer = 0
    for i in range(n):
        if traverse(answer, i, computers, visit) == True:
            answer += 1

    return answer

def traverse(group, index, computers, visit):
    if visit[index] > -1:
        return False
    
    visit[index] = group
    for i in range(len(visit)):
        if computers[index][i] == 1 and index != i:
            traverse(group, i, computers, visit)
    return True

print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))