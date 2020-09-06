num = int(input())
p = list(map(int, input().split()))
p.sort()
sum = 0
for pi in p:
    sum += num * pi
    num -= 1
print(sum)