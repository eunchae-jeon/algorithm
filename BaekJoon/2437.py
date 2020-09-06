import sys
In = sys.stdin.readline

num = int(In())
weights = list(map(int, In().split()))
weights.sort()

able = 0
for w in weights:
    if able >= w - 1:
        able += w
    else:
        break
print(able + 1)