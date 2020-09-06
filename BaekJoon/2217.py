import sys
In = sys.stdin.readline

n = int(In())
li = sorted([int(In()) for _ in range(n)])
max = 0
for i, rope in enumerate(li):
    if rope * (n - i) > max:
        max = rope * (n - i)

print(max)
