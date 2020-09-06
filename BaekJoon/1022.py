import sys
In = sys.stdin.readline

def solution():
    r1, c1, r2, c2 = map(int, In().split())
    mx = 0
    matrix = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            n = get_num(r, c)
            matrix[r-r1][c-c1] = n
            if n > mx:
                mx = n
            
    num_len = len(str(mx))
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            n_str = str(matrix[r-r1][c-c1])
            matrix[r-r1][c-c1] = " "*(num_len-len(n_str)) + n_str
        print(" ".join(matrix[r-r1]))

def get_num(i, j):
    lv = max(abs(i), abs(j))
    end = (lv*2+1)**2
    num = 0
    if i == lv:
        num = end - lv + j
    elif j == -lv:
        num = end - lv*3 + i
    elif i == -lv:
        num = end - lv*5 - j
    else:
        num = end - lv*7 - i
    return num
if __name__ == "__main__":
    solution()