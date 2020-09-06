import sys
In = sys.stdin.readline

num = In().rstrip('\n')
isZero = False
sum = 0
for c in num:
    if c =="0":
        isZero = True
    sum += int(c)
if sum % 3 == 0 and isZero == True:
    num = sorted(num, reverse=True)
    print(''.join(num))
else:
    print(-1)

    