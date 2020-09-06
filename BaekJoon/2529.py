import sys
In = sys.stdin.readline

def main():
    In()
    f = In().split()
    print(find_max(f))
    print(find_min(f))

def find_max(f):
    ans = ""
    num = 9
    cur = 9
    for c in f:
        if c == ">":
            for i in range(cur, num+1):
                ans += str(i)
            cur -= 1
            num = cur
        elif c == "<":
            cur -= 1
    else:
        for i in range(cur, num+1):
            ans += str(i)
                
    return ans

def find_min(f):
    ans = ""
    num = 0
    cur = 0
    for c in f:
        if c == "<":
            for i in range(cur, num-1, -1):
                ans += str(i)
            cur += 1
            num = cur
        elif c == ">":
            cur += 1
    else:
        for i in range(cur, num-1, -1):
            ans += str(i)
                
    return ans

main()