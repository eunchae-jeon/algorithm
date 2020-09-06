def solution(N):
    prev1 = 1
    prev2 = 1
    for _ in range(N):
        temp = prev2
        prev2 += prev1
        prev1 = temp

    return prev2*2

print(solution(6))