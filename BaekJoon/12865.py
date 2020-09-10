import sys
In = sys.stdin.readline

def solution():
    n, k = map(int, In().split())
    table = [[0] * (k+1) for _ in range(n+1)]
    for r in range(1, n+1):
        w, v = map(int, In().split())
        for c in range(1, k+1):
            prev = 0
            if c - w >= 0: prev = v + table[r-1][c-w]
            table[r][c] = max(table[r-1][c], prev)
            
    return table[n][k]

if __name__ == "__main__":
    print(solution())