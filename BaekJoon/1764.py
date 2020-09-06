N, M = map(int, input().split())
a = set(input() for _ in range(N))
b = set(input() for _ in range(M))
l = sorted(list(a & b))
print(len(l))
for p in l:   
    print(p)