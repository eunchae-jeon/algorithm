import sys
In = sys.stdin.readline

def solution():
    N = int(In())
    A = list(map(int, In().split()))
    B, C = map(int, In().split())
    answer = 0
    for a in A:
        a -= B
        answer += 1
        if a > 0:
            answer += 1 + (a-1)//C
    return answer

if __name__ == "__main__":
    print(solution())