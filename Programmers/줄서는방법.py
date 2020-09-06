def solution(n, k):
    k -= 1
    answer = []
    nums = [i for i in range(1, n+1)]
    factorial = [1]
    for i in range(1, n):
        factorial.append(factorial[-1]*i)
    for i in range(0, n):
        m = k // factorial[n-1-i]
        k %= factorial[n-1-i]
        answer.append(nums[m])
        del nums[m]
    return answer
if __name__ == "__main__":
    print(solution(3, 5))