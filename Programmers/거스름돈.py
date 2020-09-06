def solution(n, money):
    answer = 0
    dp = [[0] * (n+1) for _ in range(len(money))]
    for r in range(len(money)):
        for c in range(n+1):
            if c == 0:
                dp[r][c] = 1
            if r > 0:
                dp[r][c] = dp[r-1][c]
            if c - money[r] >= 0:
                dp[r][c] += dp[r][c-money[r]]
    answer = dp[r][c]
    return answer % 1000000007

if __name__ == "__main__":
    print(solution(5,	[1,2,5]))