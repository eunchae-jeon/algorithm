import sys
In = sys.stdin.readline

h, w = map(int, In().split())
ans = 1
if h >= 3:
    if w >= 7:
        ans = w - 2
    elif w >= 4:
        ans = 4
    else:
        ans = w
elif h == 2:
    if w >= 7:
        ans = 4
    elif w >= 5:
        ans = 3
    elif w >= 3:
        ans = 2

print(ans)