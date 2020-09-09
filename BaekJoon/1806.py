import sys
In = sys.stdin.readline

def solution():
    n, s = map(int, In().split())
    arr = list(map(int, In().split()))
    if s == 0: return 0
    l, r, subsum, answer = 0, 0, arr[0], n
    flag = False
    while True:
        if subsum < s:
            r += 1
            if r == n: break
            subsum += arr[r]
        else:
            flag = True
            answer = r - l + 1 if r - l + 1 < answer else answer
            l += 1
            if l == n: break
            subsum -= arr[l-1]
    return answer if flag else 0

if __name__ == "__main__":
    print(solution())