def solution(weight):
    weight.sort()
    able = 0
    for w in weight:
        if able + 1 >= w:
            able += w
        else:
            break
    return able + 1

print(solution([3, 1, 6, 2, 7, 30, 1]))