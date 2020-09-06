import sys
In = sys.stdin.readline
r, c = map(int, In().split())
m = [[char for char in In().rstrip()] for _ in range(r)]
pipe = []
ans = [0]

def main():
    for row in range(r):
        findPipe(row, 0)
        # printm()
    print(ans[0])

def findPipe(i, j):
    pipe.append((i, j))
    falseCount = 0
    if j+1 == c:
            ans[0]+=1
            return True
    if i > 0 and m[i-1][j+1]=='.':
        if(findPipe(i-1, j+1)):
            m[i][j] = 'o'
            return True
        else:
            falseCount += 1
    else:
        falseCount += 1
    if m[i][j+1]=='.':
        if(findPipe(i, j+1)):
            m[i][j] = 'o'
            return True
        else:
            falseCount += 1
    else:
        falseCount += 1
    if i < r-1 and m[i+1][j+1]=='.':
        if(findPipe(i+1, j+1)):
            m[i][j] = 'o'
            return True
        else:
            falseCount += 1
    else:
        falseCount += 1
    if falseCount >=3 :
        m[i][j] = 'n'
        return False


def printm():
    for row in range(r):
        print(m[row])
    print()

main()