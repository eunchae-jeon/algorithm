def solution(number, k):
    number = list(map(int, number))
    answer = ''

    idx = 0
    while idx < len(number):
        lmax = -1
        lmax_idx = 0
        if k+1+idx > len(number):
            break
        for i in range(idx, k+1+idx):
            if number[i] > lmax:
                lmax_idx = i
                lmax = number[i]
                if lmax == 9:
                    break
        
        answer += str(lmax)
        
        k -= lmax_idx - idx
        idx = lmax_idx + 1


    return answer


print(solution("69240278", 2))