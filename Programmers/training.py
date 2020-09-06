def solution(n, lost, reserve):
    res = 0
    temp = [item for item in reserve if item not in lost]
    lost = [item for item in lost if item not in reserve]
    reserve = temp
    
    lost.sort()
    reserve.sort()
    print(lost, reserve)
    i = 0
    j = 0
    while i < len(lost):
        if j >= len(reserve):
            break
        if lost[i] == reserve[j]+1 or lost[i] == reserve[j]-1:
            j += 1
            res += 1
            i += 1
        elif lost[i] > reserve[j]+1:
            j += 1
        else:
            i += 1
        
    
    return n + res - len(lost)

print(solution(8, [3, 4, 7, 8], []))