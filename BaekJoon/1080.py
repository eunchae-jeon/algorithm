import sys
In = sys.stdin.readline

def main():
    n, m = map(int, In().split())
    a = [In().rstrip() for _ in range(n)]
    b = [In().rstrip() for _ in range(n)]
    dif = list()
    num = 0
    for i in range(n):
        dif.append([])
        for j in range(m):
            if a[i][j] == b[i][j]:
                dif[i].append(0)
            else:
                dif[i].append(1)
    
    for i in range(1, n-1):
        for j in range(1, m-1):
            if dif[i-1][j-1] == 1:
                flip(dif, i-1, j-1)
                num += 1

    if isdone(dif, n, m):
        print(num)
    else:
        print(-1)
               
def flip(dif, i, j):
    for fi in range(i, i+3):
        for fj in range(j, j+3):
            dif[fi][fj] = 1 if dif[fi][fj] == 0 else 0
    #printdif(dif)

def printdif(dif):
    for d in dif:
        print(d)
    print()

def isdone(dif, n, m):
    for i in range(max(n-3, 0), n):
        for j in range(max(m-3, 0), m):
            if dif[i][j] == 1:
                return False
    return True

main()
