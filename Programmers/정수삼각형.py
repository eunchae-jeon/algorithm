def solution(triangle):
    for level in range(len(triangle)):
        for i in range(level + 1):
            if level == 0:
                continue
            
            if i == 0:
                triangle[level][i] += triangle[level-1][i]
            elif i == level:
                triangle[level][i] += triangle[level-1][i-1]
            else:
                triangle[level][i] += max(triangle[level-1][i], triangle[level-1][i-1])

    return max(triangle[level])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))