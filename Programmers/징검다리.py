def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    dists = []

    prev = 0
    for rock in rocks:
        dists.append(rock - prev)
        prev = rock
    else:
        dists.append(distance - rock)

    start = 0
    end = distance
    while start <= end:
        mid = (start + end)//2
        summ = 0
        count = 0
        for dist in dists:
            if dist + summ < mid:
                count += 1
                summ += dist
            else:
                summ = 0
        
        if count > n:
            end = mid-1
        else:
            start = mid+1
            answer = mid
            
    return answer


if __name__ == "__main__":
    print(solution(25,	[2, 14, 11, 21, 17],	2))