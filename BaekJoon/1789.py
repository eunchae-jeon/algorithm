import sys
In = sys.stdin.readline

def solution():
    s = int(In())
    n = 0
    acc = 0
    while acc <= s:
        acc += n
        n += 1
    return n-2

if __name__ == "__main__":
    print(solution())