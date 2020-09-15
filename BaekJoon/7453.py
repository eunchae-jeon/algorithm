import sys
In = sys.stdin.readline

def solution():
    answer = 0
    n = int(In())
    ab = {}
    numbers = [list(map(int, In().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            num = numbers[i][0] + numbers[j][1]#A[i] B[j]
            if num in ab:
                ab[num] += 1
            else:
                ab[num] = 1
    for i in range(n):
        for j in range(n):
            num = -(numbers[i][2] + numbers[j][3])#C[i] D[j]
            if num in ab:
                answer += ab[num]
    return answer

if __name__ == "__main__":
    print(solution())