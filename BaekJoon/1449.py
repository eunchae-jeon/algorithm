import sys
In = sys.stdin.readline

num, l = map(int, In().split())
holes = list(map(int, In().split()))

cover = -1
ans = 0
holes.sort()
for hole in holes:
    if hole > cover:
        cover = hole + l - 1
        ans += 1

print(ans)

    