num, goal = map(int, input().split())
coins = list()
for i in range(num):
    coins.append(int(input()))
num -= 1
number = 0
while goal > 0 and num >= 0:
    if coins[num] > goal:
        num -= 1

    else:
        n = goal // coins[num]
        goal -= coins[num] * n
        number += n

print(number)

