from operator import itemgetter
number = int(input())
cons = list()
for i in range(number):
    cons.append(list(map(int, input().split())))
cons = sorted(cons, key=itemgetter(1, 0))
cur = 0
ans = 0
for con in cons:
    if con[0] >= cur:
        ans += 1
        cur = con[1]

print(ans)