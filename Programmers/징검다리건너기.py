def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000
    while left <= right:
        mid = (left+right)//2
        max_conti = 0
        conti = 0
        for stone in stones:
            if stone < mid:
                conti += 1
            else:
                if conti > max_conti:
                    max_conti = conti
                conti = 0
        else:
            if conti > max_conti:
                max_conti = conti
        if max_conti < k:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer

if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))