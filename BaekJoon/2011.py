import sys
In = sys.stdin.readline

def solution():
    secret = In().rstrip()
    if secret[0] == '0': return 0
    dp = [1, 1] + [0 for _ in range(len(secret)-1)]
    for i in range(1, len(secret)):
        if int(secret[i-1] + secret[i]) <  27 and int(secret[i-1] + secret[i]) > 9:
            dp[i+1] += dp[i-1]
        if int(secret[i]) > 0:
            dp[i+1] += dp[i]
        if dp[i+1] == 0: return 0
    return dp[-1] % 1000000

if __name__ == "__main__":
    print(solution())