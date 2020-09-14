import sys
In = sys.stdin.readline

def solution():
    t = int(In())
    for _ in range(t):
        n = int(In())
        phones = [In().rstrip() for _ in range(n)]
        phones.sort()
        prev = '-1'
        for phone in phones:
            if prev == phone[:len(prev)]:
                print('NO')
                break
            prev = phone
        else:
            print('YES')
            
if __name__ == "__main__":
    solution()