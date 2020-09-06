from collections import deque


def solution(food_times, k):
    minfood = deque(sorted(food_times))
    level = 0
    sumfood = 0
    prevlevel = 0
    while True:
        try:
            minl = minfood.popleft()
        except:
            return -1
        if level < minl:
            level = minl

            if sumfood + (level-prevlevel) * (len(minfood)+1) > k:
                print(level, len(minfood))
                left = k - sumfood
                for i, food in enumerate(food_times):
                    print(i, food, left)
                    
                    if food < level:
                        continue
                    else:
                        if left == 0:
                            return i+1
                        left -=1
                    
            else:
                sumfood += (level-prevlevel) * (len(minfood)+1)
                prevlevel = level
                print("sum:{}".format(sumfood))

print(solution([3, 2, 0, 2, 3], 9))