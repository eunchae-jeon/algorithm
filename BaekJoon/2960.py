import sys
In = sys.stdin.readline

def solution():
    N, K = map(int, In().split())
    nums = set(n for n in range(2, N+1))
    count = 0
    for div in range(2, N+1):
        for n in range(2, N+1):
            if n in nums and n%div == 0:
                nums.remove(n)
                count += 1
                if count == K:
                    return n
    return

if __name__ == "__main__":
    print(solution())