def solution(n, works):
    left, right = 0, 50000
    level = 0
    diff = 0
    while left <= right:
        mid = (left + right) // 2
        time = 0
        for work in works:
            if work > mid:
                time += work - mid
        # print(time, n, left, mid, right)
        if time > n:
            left = mid + 1
            level = mid
            diff = time-n
        else:
            right = mid - 1
            

    # print(level, diff)
    answer = 0
    for work in works:
        if work >= level:
            if diff > 0:
                answer += (level+1)**2
                diff -= 1
            else:
                answer += level**2
        else:
            answer += work**2
    return answer


if __name__ == "__main__":
    # print(solution( 4,[4, 3, 3]))
    # print(solution( 1,[2, 1, 2]))
    print(solution( 3,[1,1]))