import sys
In = sys.stdin.readline

def main():
    n = int(In())
    m = [list(map(int, In().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(n):
                if k == i or k == j:
                    continue
                if m[k][j] + m[i][k] < m[i][j]:
                    print(-1)
                    return
                if m[k][j] + m[i][k] == m[i][j]:
                    break

            else:
                ans += m[i][j]

    print(ans)
main()