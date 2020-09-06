def solution(answers):
    num = [0, 0, 0]
    for i, a in enumerate(answers):
        for p in range(3):
            if a == ans(p+1, i):
                num[p] += 1

    answer = []
    for i, n in enumerate(num):
        if len(answer) == 0:
            answer.append(i+1)
        elif num[answer[-1]-1] == n:
            answer.append(i+1)
        elif num[answer[-1]-1] < n:
            answer = [i+1]
        
    return answer

def ans(p, i):
    if p == 1:
        return (i%5) + 1
    elif p == 2:
        idx = i%8
        if i%8 == 1:
            return 1
        elif i%8 == 3:
            return 3
        elif i%8 == 5:
            return 4
        elif i%8 == 7:
            return 5
        else:
            return 2
    elif p == 3:
        idx = (i%10)//2
        if idx == 0:
            return 3
        elif idx == 1:
            return 1
        elif idx == 2:
            return 2
        elif idx == 3:
            return 4
        else:
            return 5

    #12345
    #21232425
    #3311224455

print(solution([1,3,2,4,2]))